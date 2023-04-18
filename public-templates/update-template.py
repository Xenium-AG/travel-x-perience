import re, math

# define the input file
input_file = 'besuchte-laender.tsv'

# define the final output file to be manipulated
target_file = "index-unencrypted.html"

# define dictionaries to hold the contributors and reports
contributors = {}
reports = {}

# keep track of sections in the input file
report_section = False

# list of all countries to be considered
all_countries = "AD, AE, AF, AG, AI, AL, AM, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BM, BN, BO, BQ, BR, BS, BT, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW".split(', ')

# default link for all countries with a report
default_link = "#"

# open the input file and read it line by line
with open(input_file, 'r') as f:
	for line in f:
		# check for new section
		if "---reports---" in line:
			report_section = True
			continue

		# ignore any line that starts with //
		if line.startswith('//'):
			continue
		
		# replace "https://www" with "www"
		line = line.replace('https://www', 'www')
		
		# remove any text starting with //
		line = re.sub(r'//.*', '', line)
		
		# print(line)
		
		# strip whitespace from the line
		line = line.strip()
		
		if not report_section:
			# ignore lines that do not contain "amcharts.com"
			if 'amcharts.com' not in line:
				continue
			
			# remove "...com/#" from any line
			line = line.replace('...com/#', '')
			
			# split the line into a list of values
			person, countries = line.split('\t')
			
			# convert the values to a dictionary
			contributors[person] = countries.split(',')

		else: #if report_section
			if '\t' not in line:
				continue
			
			# split the line into a list of values
			country, report = line.split('\t')
			
			# store report string in dict
			reports[country] = report
			

# print the output dictionary
# print(people)

# define a dictionary to hold the countries
countries = {}

# iterate over each name and code in the people dictionary
for person, values in contributors.items():
	# iterate over each code in the list of codes for this name
	for country in values:
		# if the code is not already a key in countries, create a new array for it
		if country not in countries:
			countries[country] = []
		# append the name to the array for this code
		countries[country].append(person)

# print the countries dictionary
# print(countries)

# generate javascript code for the country arrays
js = ""
for country in all_countries:
	if(js): # new line if necessary
		js += '\n'
	
	js += "\t\t\t\t" # indenting for html

	# get array of all people who visited that country
	people = sorted(countries.get(country, []))

	# comment out if nobody was here
	if not (len(people) > 0 or country in ["DE", "AT"]):
		js += "// "

	js += country + ": {" # create js object

	# special color for DE and AT
	if country in ["DE", "AT"]:
		js += "color: '#ffa05f', "

	# how many people visited here?
	if country == "DE": # or for DE: How many contributors do we have?
		js += "visitors: " + str(len(contributors)) + ", "
	else:
		js += "visitors: " + str(len(people)) + ", "

	# generate list of all people with custom strings for DE and unvisited countries
	js += "list: '"
	if country == "DE":
		js += "everyone"
	elif len(people) == 0:
		js += "nobody"
	else:
		js += ", ".join(people)
	js += "'"

	# get report string for that country
	report = reports.get(country, "")
	if report != "":
		js += ", recording: '" + report + "'"

	# add default_link to countries with a report
	if report != "":
		js += ", link: '" + default_link + "', " + "linkTarget: '_blank'"

	js += "}," # finish js object

# print(js)

# Injects a text into an existing file between startline and endline
# (or just overrides the line after startline, if no end is given)
def inject(text, startline, endline = None, file = target_file):
	# open the input file
	with open(file, "r") as f:
		lines = f.readlines()

	# find the indices of the start and end lines
	start_index = -1
	end_index = -1
	for i, line in enumerate(lines):
		if startline in line:
			start_index = i
		if endline is not None and endline in line:
			end_index = i
	
	if endline is None:
		end_index = start_index + 2

	# if we found the start and end lines, inject the JavaScript string between them
	if start_index != -1 and end_index != -1:
		lines = lines[:start_index+1] + [str(text) + '\n'] + lines[end_index:]
	else:
		print("ERROR: COULD NOT FIND PARSING STRINGS!!!")

	# write the modified lines back to the file
	with open(file, "w") as f:
		f.writelines(lines)

# inject js string as parsing list
inject(js, "// START OF AUTOMATED PARSING LIST", "// END OF AUTOMATED PARSING LIST")

# inject total count of countries
inject("						" + str(len(countries)), "<!--TOTAL COUNT-->")

# inject goal for country count
goal = len(countries) + 1
goal = math.ceil(goal / 10.0) * 10
inject("						" + str(goal) + "?", "<!--NEXT GOAL-->")