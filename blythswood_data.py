"""
Blythswood AI - Hardcoded Data
Master doc + automatic loading of example grants
"""

import os

MASTER_DOC = """BLYTHSWOOD CARE - API-OPTIMIZED MASTER DOCUMENT FOR GRANT APPLICATIONS
Generated: November 19, 2025
Purpose: LLM API reference for automated grant application generation
Structure: Machine-readable with grant-relevant categorization

================================================================================
SECTION 1: LEGAL AND REGISTRATION DATA
================================================================================

LEGAL_ENTITY_PRIMARY:
  Name: Blythswood Care
  Charity_Number_Scotland: SC048001
  Company_Number_UK: SC583493
  Legal_Structure: Scottish Charitable Incorporated Organisation (SCIO)
  Registration_Date: 2018-04-16 (current SCIO structure)
  Predecessor_Entity: Blythswood Care 1993 (SC021848, registered 1993-09-13)
  Tax_Status: Registered charity (tax exempt)
  VAT_Status: Not specified in public records
  
LEGAL_ENTITY_SUBSIDIARIES:
  Subsidiary_1:
    Name: Blythswood Trading Limited
    Type: Trading subsidiary (wholly owned)
    Purpose: Retail operations, charity shops, goods recycling
    Turnover_2023: £2,429,000
    
  Subsidiary_2:
    Name: Blythswood Ireland Limited
    Charity_Number_NI: NIC104515
    Company_Number_NI: NI050683
    Legal_Structure: Company limited by guarantee
    Member: Blythswood Care (sole member)
    Consolidated_Since: 2021-01-01
    Turnover_2023: £1,120,000
    
REGISTERED_ADDRESSES:
  Headquarters:
    Address_Line_1: Highland Deephaven Industrial Estate
    Address_Line_2: Evanton
    City: Dingwall
    County: Ross-shire
    Postcode: IV16 9XJ
    Country: Scotland
    Phone: 01349 830 777
    Email: info@blythswood.org
    
  Glasgow_Depot:
    Address: 32 Dalziel Road, Hillington Park
    City: Glasgow
    Postcode: G52 4NN
    Phone: 0141 882 0585
    Email: glasgowdepot@blythswood.org
    
  Northern_Ireland_Office:
    Address: 93 Templepatrick Road, Ballyclare
    County: Co Antrim
    Postcode: BT39 9RQ
    Phone: 028 93 349 859
    Email: enquiries.ireland@blythswood.org

REGULATORY_COMPLIANCE:
  OSCR_Registered: Yes
  OSCR_Annual_Returns: Filed on time (all years)
  Companies_House_Status: Active
  Confirmation_Statement: Up to date
  Member_Organizations:
    - Circular Communities Scotland (CCS)
    - Charity Retail Association (CRA)
    - Trussell Trust (foodbank partner/franchisee)

================================================================================
SECTION 2: GOVERNANCE AND LEADERSHIP
================================================================================

BOARD_OF_TRUSTEES:
  Chairman:
    Name: David Kemlo Laing
    Appointed: 2018-08
    Role: Non-executive chairman
    
  Chief_Executive:
    Name: Jeremy Edward Ross
    Appointed: 2024-02-01 (as CE); 2021-02 (as trustee)
    Previous_Role: Free Church minister (16 years)
    Blythswood_History: Worked 1998-2007 as fundraiser/area coordinator
    Relationship_to_Founder: Son of Rev Jackie Ross (founder)
    Born: 1976-04
    
  Trustees_List:
    - Nathan Alexander Hawthorne (2025-02)
    - Rev Gordon James Mackay (2024-05)
    - Iain Maclelland (2024-05)
    - Kate-Marie Macrae (2024-02)
    - Richard John McCallum (2022-03)
    - Lorne Helen Gowers Millar (2024-08)
    - Lorimer Gray (longstanding)

SENIOR_MANAGEMENT_TEAM:
  Chief_Operating_Officer:
    Name: Paul Macleod
    Tenure_Start: 2009
    Responsibilities: 23 Scottish charity shops, 2 hub depots, retail operations
    Background: Private sector experience
    
  Head_of_Retail:
    Name: Alan
    Tenure_Start: 2020
    Experience: 30 years retail leadership
    Responsibilities: Network of 26 charity shops (24 operational)
    Notable: Former atheist, came to faith 2008
    
  Executive_Director_Romania:
    Name: Balazs Csiszer
    Location: Cluj, Romania
    Responsibilities: All Romanian project operations, partnerships
    Oversight: Daniel Centre, Talita Kum coordination
    Succession: Took over from Finlay Mackenzie (retired 2023)

FORMER_KEY_PERSONNEL:
  James_Campbell:
    Role: Chief Executive
    Tenure: 1998-2024 (26 years)
    Retirement: 2024-01-31
    Notable_Achievement: Transformed organization during tenure
    
  Danny_Muschate:
    Role: Head of Fundraising & Marketing
    Tenure: 2007-2023 (16 years)
    Background: 9 years NHS Highland
    Key_Achievement: Shoebox Appeal promotional materials, school trips to Romania
    
  Finlay_Mackenzie:
    Role: Head of Projects
    Tenure: 1993-2023 (30 years)
    Achievement: Established international partnerships

TRUSTEE_REMUNERATION:
  Policy: None (all volunteer)
  Expenses_2023: £0
  Trustee_Donations_2023: £4,283 (from 6 trustees)
  Trustee_Donations_2022: £960 (from 6 trustees)

================================================================================
SECTION 3: FINANCIAL DATA AND ANALYSIS
================================================================================

FINANCIAL_SUMMARY_5_YEARS:
  Year_2020:
    Income: 7668376
    Expenditure: 6487950
    Net: 1180426
    Surplus_Rate: 15.4%
    
  Year_2021:
    Income: 10111470
    Expenditure: 9515953
    Net: 595517
    Surplus_Rate: 5.9%
    
  Year_2022:
    Income: 10408636
    Expenditure: 10176759
    Net: 231877
    Surplus_Rate: 2.2%
    Peak_Year: True
    
  Year_2023:
    Income: 9627158
    Expenditure: 9507064
    Net: 120094
    Surplus_Rate: 1.2%
    Year_on_Year_Change: -7.5%
    
  Year_2024_Projected:
    Income: 8394140
    Expenditure: 8533395
    Net: -139255
    First_Deficit: True
    Year_on_Year_Change: -12.8%

INCOME_BREAKDOWN_2023:
  Donations_Cash: 2015621 (20.94%)
  Legacies: 275803 (2.86%)
  Trading_Income: 3486844 (36.22%)
  Investment_Income: 6437 (0.07%)
  Gift_in_Kind_Donated_Goods: 3842453 (39.91%)
  Total: 9627158
  
INCOME_SOURCES_CATEGORIZED:
  Individual_Donations: 48% (includes cash donations and legacies)
  Earned_Income: 31% (shops, events, trading)
  Grant_Funding: 21% (trusts, foundations, statutory)
  
EXPENDITURE_BREAKDOWN_2023:
  Christian_Literature: 127044 (1.34%)
  Direct_Project_Costs: 707533 (7.44%)
  Special_Projects_Support: 871236 (9.16%)
  Trading_Costs: 3326530 (34.99%)
  Support_Costs: 205647 (2.16%)
  Fundraising_Costs: 426621 (4.49%)
  Gift_in_Kind_Donated_Goods: 3842453 (40.42%)
  Total: 9507064

FINANCIAL_POSITION_2023:
  Cash_in_Bank: 1320000
  Total_Assets: 3250000
  Total_Liabilities: 614450
  Net_Assets: 2640000
  Debt_Ratio: 19%

FINANCIAL_EFFICIENCY_METRICS:
  Administrative_Overhead: ~4% (exceptionally low)
  Program_Spending_Ratio: ~96%
  Reserves_Policy: Sufficient for working capital and ongoing activities
  Fundraising_ROI: Not specified but historically strong
  Grant_Success_Rate_Historical: 78%

FINANCIAL_TRENDS_AND_RISKS:
  Declining_Income_Trend: -19.4% from peak (2022 to 2024)
  Primary_Risk: Financial sustainability
  Mitigating_Factors:
    - Diverse income streams
    - Low overhead costs
    - Strong reserves position
    - Established donor base
  Future_Funding_Needs: Sustainable long-term funding beyond short-term grants

================================================================================
SECTION 4: WORKFORCE AND VOLUNTEER DATA
================================================================================

EMPLOYEES:
  Total_Staff_2023: 143
  Total_Staff_Historical: ~120
  Highland_Region_Staff: 90
  Staff_Categories:
    - Retail staff (charity shops)
    - Warehouse and logistics
    - Foodbank coordinators
    - Project management
    - Fundraising and marketing
    - Administration
    
VOLUNTEERS:
  Total_Active_Volunteers: 1000+ (across UK and NI)
  Volunteer_to_Staff_Ratio: >10:1
  Total_Volunteer_Hours_2023: 30000+
  Economic_Value_2023: £310000+ (calculated at National Living Wage)
  
VOLUNTEER_ROLES:
  - Shoebox checking and sorting
  - Charity shop staff
  - Foodbank support
  - Fundraising events
  - Goods sorting at depots
  - Vehicle driving
  - Summer camp leadership (Romania)
  - Skills-based volunteering (professional services)
  - Marking Bible correspondence courses
  - Public speaking and presentations
  
VOLUNTEER_DEMOGRAPHICS:
  Age_Range: All ages
  Geographic_Distribution: Great Britain and Northern Ireland
  Church_Partnerships: 15+ churches involved in shoebox sorting (example: Fullarton Centre)

================================================================================
SECTION 5: PROGRAM OPERATIONS - SHOEBOX APPEAL
================================================================================

PROGRAM_NAME: Christmas Shoebox Appeal
PROGRAM_CODE: SB01
ESTABLISHED: 1993
DURATION: 31+ years

ANNUAL_METRICS_RECENT:
  Year_2022: 88816 boxes
  Year_2023: 84655 boxes (reported in annual report)
  Year_2023_Alt: 89000 boxes (reported in other sources)
  Lifetime_Total: 2739772 boxes (as of 2023)
  Average_Annual: ~88000 boxes

DISTRIBUTION_COUNTRIES:
  Primary_Recipients:
    - Albania
    - Bulgaria
    - Hungary
    - Kosovo
    - Moldova
    - Romania
    - Serbia
    - Ukraine (especially since 2022)
    
RECIPIENT_CATEGORIES:
  - Schools
  - Hospitals
  - Orphanages and care homes
  - Low-income households
  - Internally Displaced Persons (Ukraine)
  - Roma communities
  
BOX_CONTENTS_STANDARD:
  Toiletries: [toothbrush, toothpaste, soap, shampoo]
  Warm_Items: [hat, scarf, gloves]
  Stationery: [pencils, notebooks, coloured pencils]
  Toys: [small toys, games]
  Sweets: [confectionery]
  Clothing: [underwear, socks]
  Christian_Literature:
    Children: Bible story book
    Teenagers: Testimony booklet
    Adults: Calendar with verses
    
CHRISTIAN_LITERATURE_PRODUCTION_2023:
  Children_Book: "Job the Patient Friend" by Carine Mackenzie
  Teen_Book: "Turning Point" - testimony of Ebbie Israel
  Adult_Item: "Words of Life" calendar (Trinitarian Bible Society)
  Languages: 6 (Albanian, Bulgarian, Hungarian, Romanian, Serbian, Ukrainian)
  Total_Items_Purchased: 123500
  Total_Cost: £50300
  Cost_Per_Item: £0.41
  Partner: Christian Focus Publications
  
LOGISTICS:
  Donation_Requirement: £3 minimum per box (transport costs)
  Collection_Deadline: Late October/early November
  Delivery_Timeframe: Before Christmas
  Total_Aid_Transported_2023: 322 tonnes
  Shoebox_Weight_2023: 154 tonnes
  Other_Aid_2023: 168 tonnes (fire engines, rescue equipment via SERA)
  
VOLUNTEER_EFFORT_EXAMPLE:
  Location: Fullarton Centre, Ayrshire
  Boxes_Processed: 6000
  Duration: 5-7 days
  Volunteers: 80+
  Churches_Represented: 15+
  Tasks: Checking boxes, inserting literature, packaging
  
IMPACT_SIGNIFICANCE:
  Largest_Christian_Literature_Project: Yes
  Gospel_Outreach_Vehicle: Primary method for literature distribution
  Community_Engagement: Extensive school and church involvement

================================================================================
SECTION 6: PROGRAM OPERATIONS - UK FOODBANKS
================================================================================

PROGRAM_NAME: Foodbank Network
PROGRAM_CODE: FB01
ESTABLISHED: 2005
PARTNERSHIP: Trussell Trust (franchisee)
DURATION: 19+ years

GEOGRAPHIC_COVERAGE:
  Highland_Region:
    Primary_Centre: 1 Glebe Street, Inverness IV1 1RF
    Phone: 01463 717 630
    Email: foodbank@blythswood.org / foodbank.admin@blythswood.org
    Operating_Hours: Monday-Friday 12:00-14:00 (collection)
    Office_Hours: Monday-Friday 09:00-15:00
    
  Highland_Network_Locations:
    - Inverness (primary)
    - Alness
    - Aviemore
    - Dingwall
    - Kyle of Lochalsh
    - Nairn
    - Tain
    - Thurso
    - Wick
    
  Edinburgh:
    Location: Southeast Edinburgh
    Foodbank_Manager: Miriam Montgomery
    
USAGE_STATISTICS:
  Lifetime_Beneficiaries: 70000+ (since 2005)
  
  Year_2023:
    Highland_Total: 6406 people
    Edinburgh_SE: 3788 people
    Combined: 10194 people
    
  Year_2024_Jan_Dec:
    Highland_Combined: 5434 people
    Year_on_Year_Change: -15%
    Reason_for_Decrease: CAB advisor funding (early intervention)
    
  Year_2024_Jan_Aug:
    Inverness_Area: 2072 people
    
  Financial_Year_2023_24_Apr_Mar:
    Inverness_Area: 3170 people

FOOD_DISTRIBUTED:
  Year_2023_Highland: 65.6 tonnes
  Year_2023_Edinburgh: 38.1 tonnes
  Year_2023_Combined: 103.7 tonnes
  Package_Type: 3-day emergency food supply
  
REFERRAL_SYSTEM:
  Partner_Agencies: 100+
  Referral_Sources:
    - Highland Council Care Health and Social Care Service
    - Service Points
    - Housing Services
    - Scottish Welfare Fund
    - Citizens Advice Bureaux
    - Women's Refuge
    - Health Visitors Team
    - Medical teams
    
REASONS_FOR_USE:
  - Benefit delays
  - Low income
  - Changes to benefits
  - Unexpected bills
  - Redundancy
  - Mental health crises
  - Family crisis situations
  - Marriage/relationship breakdown
  
CLIENT_SUPPORT:
  Emergency_Food: 3-day nutritionally balanced packages
  Listening_Service: Trained staff and volunteers
  Signposting: Referrals to other support agencies
  Home_Delivery: Available for those unable to visit centres
  CAB_Advisor: On-site support (funded by Trussell Trust additional funding)
  Pet_Food: Partnership with Edinburgh Dog and Cat Home
  
FACILITY_DETAILS_INVERNESS:
  Address: 1 Glebe Street (shared building with charity shop)
  Features:
    - Separate entrance for privacy
    - Private meeting room
    - Dedicated storage space
    - Receiving and sorting area
  Accessibility: Wheelchair accessible with ramp and on-site parking
  Host_Location_Historical: Madras Street Mission Hall (Free North Church)
  
PERMANENT_COLLECTION_POINTS:
  - Tesco Inshes, Inverness
  - Tesco Tain
  - Asda Inverness
  - Asda Tain
  - All Blythswood charity shops
  
FUNDING_REQUIREMENTS:
  Inverness_Common_Good_Fund_Application_2024: £25000
  Purpose: Running costs offset
  Justification: Rising expenses, cost of living crisis
  Status: Recommended for approval
  
GOVERNANCE_CHANGES:
  New_Governance_Structure: In process (2025)
  Potential_Handover: New organization being established
  Continuity_Plan: Unspent grants to transfer to new entity

================================================================================
SECTION 7: PROGRAM OPERATIONS - ROMANIA PROJECTS
================================================================================

COUNTRY: Romania
BLYTHSWOOD_ROMANIA_ESTABLISHED: 1995
RELATIONSHIP_FOUNDATION: Rev Jackie Ross met Reformed Pastor Levente Horvath (1980s)
FIRST_AID_DELIVERIES: 1990 (post-communism)

---

PROJECT_1_DANIEL_CENTRE:
  Program_Code: RO-DC01
  Location: Cluj-Napoca, Romania
  Established: 2000
  Founder: Rev Jackie Ross
  Project_Type: Residential care and life skills training
  
  Target_Population:
    - Young men (ages 18-25)
    - Care leavers (ex-orphanage system)
    - Vulnerable to homelessness and unemployment
    
  Capacity: 5-7 residents typically
  
  Accommodation:
    Type: Self-contained studio flats (renovated 2018)
    Renovation_Team: Go Relief (Northern Ireland volunteers)
    Purpose: Independent living skills development in safe environment
    
  Services_Provided:
    - Accommodation and utilities
    - Life skills training (cooking, budgeting, household management)
    - Employment support and job search
    - Financial literacy and money management
    - Social worker support (Lujza Fechita)
    - After-care meetings (Friday nights)
    - English language tutoring
    - Access to kitchen and cooking facilities
    - Educational and vocational guidance
    
  Success_Indicators:
    - Employment placement
    - Social housing waiting list placement
    - Independent living transition
    - Sustained employment
    - Continued education (e.g., computer programming college)
    
  Notable_Outcomes:
    - Residents gain employment (e.g., fast food outlets, security work)
    - English language proficiency achieved in 6 months (example cases)
    - Transition to social housing
    - After-care community maintained
    
  Challenges_Addressed:
    - Modern slavery rescue and rehabilitation
    - Mental health support
    - Substance abuse recovery
    - Trauma from care system
    - Lack of family support
    
  Current_Issues:
    - Staff burnout risk (former residents as carers)
    - Complex psychiatric cases
    - Drug dependency management
    - Behavioral challenges requiring dismissal

---

PROJECT_2_TALITA_KUM:
  Program_Code: RO-TK01
  Location: Jimbolia, Western Romania (near Serbian border)
  Established: 2001
  Program_Name_Meaning: "Get up, little girl" (Aramaic)
  Project_Type: After-school educational support
  
  Management:
    Director: Adrian Popa
    Assistant: Ritta Popa
    Teacher: Carmen Popa
    Additional_Staff: Adrian's daughter (returned from pregnancy leave)
    
  Sub_Programs:
    TK1:
      Target_Age: Primary school children
      Current_Enrollment: 35 children
      
    TK2:
      Target_Age: 10-15 years (junior secondary)
      Current_Enrollment: 45 children
      Purpose: Extended support through secondary education
      
    TK3:
      Target_Age: High school students
      Current_Enrollment: ~10 graduated students
      Status: Fledgling program
      Purpose: High school support and vocational training
      
  Total_Current_Beneficiaries: 70+ children (plus TK3)
  
  Ethnic_Composition: ~50% Roma background, multiethnic
  
  Services_Provided:
    - Two nutritious meals daily
    - Homework assistance
    - One-on-one remedial tutoring
    - Shower facilities
    - Clothing wash facilities
    - Notebooks and school supplies
    - Music tuition
    - IT training
    - Puppet theatre
    - Craft activities
    - Summer camps (week-long, Carpathian mountains)
    
  Educational_Outcomes:
    - Catch-up education (e.g., 1 year in 2 months)
    - Grade advancement despite challenges
    - Prevention of school dropout
    - Homework completion support
    - Improved attendance
    
  Social_Outcomes:
    - Prevention of premature marriage
    - Reduction in juvenile delinquency
    - Prevention of unregistered child labor
    - Improved social interaction skills
    - Confidence building
    
  Summer_Camps:
    Frequency: Annual
    Duration: 1 week
    Location: Southern Carpathian mountains (Retezat mountains)
    TK1_Timing: Late June
    TK2_Timing: August
    Volunteer_Support: S5 pupils from Inverness schools
    Activities: Hiking, games, crafts, Bible stories, meals, adventure parks
    Partner: Children for Christ
    
  Children's_Day_Show:
    Frequency: Annual
    Location: Jimbolia main square
    Purpose: Community engagement and celebration
    
  Funding_Model:
    Annual_Operating_Cost: ~€50000
    Historical_Support: Suits on Bikes charity cycle (10th anniversary 2013)
    Capital_Support: European Regional Development Fund (school building)
    
  Staffing_Challenges:
    - Romanian teachers' strikes impact
    - Salary competitiveness with government positions
    - Staff retention
    
  Impact_Examples:
    - Children 3 years behind grade level making progress
    - Homeless families' children attending daily
    - Prevention of care system placement
    - University aspirations (e.g., law, music)
    
  20th_Anniversary: 2021
  Expansion_Plans: Vocational training opportunities

---

PROJECT_3_BASIS:
  Program_Code: RO-BA01
  Location: Cluj area, Romania
  Project_Type: Food distribution program
  
  Services:
    - Monthly food packages
    - Household essential support
    - Medical expense assistance
    
  Beneficiaries: 30 families (within 50km radius of Cluj)
  
  Target_Population:
    - Elderly with health issues
    - Grandparents raising grandchildren
    - Families in extreme poverty
    - Those at risk of child protection intervention
    
  Manager: Agnes Csiszer
  
  Prevention_Focus: Keeping children in family settings vs. orphanages
  
  Typical_Household_Income: £350 per month (example case)
  
  Service_Duration: Long-term support until circumstances change

---

ROMANIA_SUPPORT_INFRASTRUCTURE:
  Executive_Director: Balazs Csiszer
  Location: Cluj
  Oversight_Transition: From Finlay Mackenzie (2023)
  Assessment: Very positive initial review by James Campbell
  
  Property_Matters:
    Cluj_Depot: Sale in progress (not completed as of 2024)
    Rental_Apartments: Daniel Centre graduate housing
    
  Staff_Support:
    Ukrainian_Coordinator: Olga (parents relocated to Cluj from Ukraine)
    
  Summer_Camp_Coordination:
    Countries: Romania, Moldova, Serbia
    Partner_Organizations: Children for Christ, other Christian ministries
    
  Inverness_School_Trips:
    Schools_Involved: 3 Inverness schools
    Participants: S5 pupils
    Purpose: Summer camp volunteer support
    Organizer_Historical: Danny Muschate (fundraising head)
    Timing: August
    Duration: Week-long
    Activities: Running camps for deprived children

================================================================================
SECTION 8: PROGRAM OPERATIONS - INTERNATIONAL (NON-ROMANIA)
================================================================================

ACTIVE_COUNTRIES: 13 (with trusted partners)
ADDITIONAL_DISTRIBUTION: 8 countries (goods, money, literature)
TOTAL_INTERNATIONAL_REACH: 21+ countries

---

INDIA_CORNERSTONE_TRUST:
  Program_Code: IN-CT01
  Location: Mumbai (Navi Mumbai)
  Partner_Organization: Cornerstone Trust
  Director: Asmita Vadavana
  
  Context: Red-light district ministry
  Target_Population: Women and children in red-light districts
  
  Services:
    - Foster care placements
    - Day centre programs
    - Gospel outreach
    
  Current_Beneficiaries:
    Foster_Care_Girls: 5
    Day_Centre_Children: 20
    Total: 25 children
    
  Foster_Care_Support:
    - Three cooked meals daily
    - Health monitoring
    - Education (school fees, supplies)
    - Sports activities
    
  Outcomes:
    - Malnutrition recovery
    - School grade progression
    - Health problem resolution
    - Physical activity participation
    
  Gift_Catalogue_Support: Yes
  
  New_Project_Beacon_Centre:
    Location: Turbe, Navi Mumbai
    Opened: December 2022
    Services:
      - Culinary training
      - Sports training
      - Toddlers' groups
      - Garden club
      - Career guidance
    Extension_Plans: Child development centre in Shramik Nagar
    
  Bible_Distribution:
    Languages: Bengali, English, Hindi, Marathi
    Recipients: Women and children at Cornerstone

---

KENYA_SARGY_EDUCATION_CENTRE:
  Program_Code: KE-SE01
  Location: Rusinga Island, Kenya
  Project_Name: Sargy Education Centre
  Director: Samwel Okomo
  
  Beneficiaries: 350 children
  
  Target_Population:
    - Children living below international poverty line (<$1/day)
    - Children of unqualified workers (e.g., firewood gatherers)
    - Grandparent-headed households
    
  Services:
    - Cooked meals (5 days/week)
    - School placement
    - Educational supplies
    
  Meal_Composition: Beans, rice, ugali, green vegetables, maize
  Nutritional_Standard: Balanced diet meeting children's needs
  
  Educational_Outcomes:
    - Daily school attendance
    - Academic progress
    - Prevention of malnutrition
    
  Gift_Catalogue_Support: Yes

---

HUNGARY_BONUS_PASTOR_FOUNDATION:
  Program_Code: HU-BP01
  Location: Ozd, Hungary
  Established: 1993
  Project_Type: Addiction recovery and treatment
  
  Services:
    - Long-term therapy
    - Treatment programs
    - Camps
    - Counselling
    - Specialist training
    
  Addictions_Addressed:
    - Drug addiction
    - Alcohol addiction
    - Other dependencies
    
  Duration: 30+ years of operation

---

SERBIA_OPERATIONS:
  Coordinator: David Armus
  
  Christianity_Explored_Program:
    Material: Serbian edition (published 2 years ago)
    Distribution: 40 groups in 18 locations
    Participants: 264 total
    Church_Types: Baptist, Pentecostal, Evangelical Roma
    Sponsor: Blythswood Care
    Impact: Improved inter-church cooperation
    
  Shoebox_Distribution:
    Partner: Faton Barisha
    Example_Distribution: 200 households (Roma community near Gjakova)

---

KOSOVO_OPERATIONS:
  Distribution_Focus: Roma communities
  Partner_Example: Faton Barisha (Gjakova area)
  Winter_Climate: Severe (minus 10°C, heavy snow)
  Poverty_Level: Extreme
  Family_Size: 5-11 children typical
  
  Box_Recipients:
    - Children (toys, clothes, stationery)
    - Adults (hygiene items, underwear, socks)

---

UKRAINE_OPERATIONS:
  Status: Ongoing crisis response (since 2022)
  Emergency_Appeal_2022: Raised £735000+
  
  Primary_Recipients:
    - Internally Displaced Persons (IDPs)
    - Returning residents (e.g., Kyiv district, Borodianka)
    - Children affected by conflict
    
  Aid_Types:
    - Christmas shoeboxes
    - Emergency equipment
    - Specialized aid
    - Food packages
    - Practical support
    
  Partner_Coordination:
    Coordinator: Olga (based in Cluj, Romania)
    Christian_Aid_Partnership: Some Ukrainian partners (ending Feb 2025)
    Accountability: High standards required
    
  Fire_Equipment_Distribution:
    Partner: SERA (Scottish Emergency Relief Agency)
    Volume_2023: Majority of 168 tonnes non-shoebox aid
    Destination: Primarily Ukraine, some Moldova
    
  Medium_Term_Planning: Under development
  
  Impact_Example:
    Location: Borodianka (60km NW of Kyiv)
    Context: Town partially destroyed in invasion
    Recipients: Families returning to damaged homes
    Response: Christmas boxes, practical gifts
    
  Continued_Needs: Uncertainty about return home, ongoing displacement

---

MOLDOVA_OPERATIONS:
  Activities:
    - Summer camps (Children for Christ partnership)
    - Shoebox distribution
    - Emergency equipment (spillover from Ukraine aid)

---

ALBANIA_BULGARIA_OPERATIONS:
  Primary_Activity: Shoebox distribution
  Schools: Yes
  Hospitals: Yes
  Care_Homes: Yes

---

AFRICA_GENERAL:
  Literature_Distribution: Bibles, tracts
  Partner_Organizations: India Bible Literature (recipient of unsold books)
  Example_Grant: 48 Chichewa Bibles (Malawi)

================================================================================
SECTION 9: CHRISTIAN LITERATURE AND MINISTRY
================================================================================

MINISTRY_FOCUS: Advancement of Christian religion
LITERATURE_STRATEGY: Distribution through multiple channels
TOTAL_LITERATURE_EXPENDITURE_2023: £127044 (1.34% of total spending)

---

SHOEBOX_LITERATURE:
  Annual_Scale: Largest Christian literature project
  Items_2023: 123500
  Languages: 6
  Cost_2023: £50300
  Average_Cost_Per_Item: £0.41
  
  Publications_2023:
    Children:
      Title: "Job the Patient Friend"
      Author: Carine Mackenzie
      Format: Bible story retelling
      
    Teenagers:
      Title: "Turning Point"
      Content: Testimony of Ebbie Israel
      
    Adults:
      Title: "Words of Life"
      Type: Calendar with verses
      Publisher: Trinitarian Bible Society
      
  Publishing_Partner: Christian Focus Publications
  Languages: Albanian, Bulgarian, Hungarian, Romanian, Serbian, Ukrainian

---

BIBLE_DISTRIBUTION:
  India:
    Languages: Telugu (250), Tamil (200), Bengali, English, Hindi, Marathi
    Recipients: Pastors, women and children at Cornerstone
    
  Malawi:
    Language: Chichewa (48 Bibles)
    
  UK:
    Distribution: Schools, prisons (historical)
    
  Seafarers:
    Location: Invergordon Parish Church Seafarers' Centre
    Languages: 15 total (Croat, English, French, German, Hindi, Hungarian, Italian, Korean, Latvian, Spanish, Portuguese, Russian, Tagalog, Tamil, Ukrainian)
    Format: Bibles, New Testaments, other literature
    
  Historical_Scale:
    1970s: 20000 Bibles per printing
    Destinations: Africa, India, Eastern Bloc, UK schools, prisons

---

LITERATURE_GRANTS_2023:
  Total_Grants: 109
  Unique_Grantees: 69
  Countries: 10
  
  Tract_Distribution:
    English_Tracts: 27000+
    Locations: UK and overseas
    
  Bible_Distribution_Detail:
    India_Telugu: 250
    India_Tamil: 200
    Malawi_Chichewa: 48
    India_Cornerstone: Multiple languages
    
  Grant_Recipients:
    - Pastors in India
    - Mumbai projects
    - Malawi church leaders
    - UK distribution networks

---

CHRISTIANITY_EXPLORED_PROGRAM:
  Location: Serbia
  Format: Course booklets and DVDs
  Edition: Serbian translation
  Sponsor: Blythswood Care funding
  
  Distribution_Since_Publication: 2 years
  Groups: 40
  Locations: 18
  Participants: 264
  
  Church_Reach:
    - Baptist churches
    - Pentecostal churches
    - Evangelical Roma churches
    
  Impact:
    - Deepened doctrinal understanding
    - Improved inter-church cooperation
    - Spiritual growth of participants
    - Assurance of salvation
    
  Example_Testimony:
    Participant: Andrija (age 20)
    Location: Near Niš, southern Serbia
    Background: Existing believer
    Outcome: Deeper understanding of sin/salvation doctrines
    Future: Music university aspirations

---

CHARITY_SHOP_BOOK_SALES:
  Strategy: Seasonal Christian book selections
  Source: 10ofthose.com
  Pricing: Bargain prices
  Seasons: Easter, summer, Christmas
  
  Challenges: Lower sales than desired
  Alternative_Use: Donated to India Bible Literature (2 pallets)
  Distribution_Route: Belfast contacts

---

BIBLE_CORRESPONDENCE_COURSES:
  Volunteer_Activity: Marking courses
  Historical: Longstanding program
  Current_Status: Ongoing

---

HISTORICAL_PUBLISHING:
  1970s_Activity: Printing Bibles (20000 per run)
  Bookshops: Established across Scotland, England, Northern Ireland
  Book_Vans: Mobile distribution
  Agencies: Distribution network

---

FOUNDER'S_ORIGINAL_WORK:
  Organization_Name: Blythswood Tract Society
  Year: 1966
  Activity: Street evangelism, Christian literature distribution
  Location: Blythswood Square, Glasgow
  Founders: Rev Jackie Ross, Donald Ross, Ian Tallach, John Tallach

================================================================================
SECTION 10: RETAIL AND TRADING OPERATIONS
================================================================================

TRADING_SUBSIDIARY: Blythswood Trading Limited
IRELAND_SUBSIDIARY: Blythswood Ireland Limited

CHARITY_SHOP_NETWORK:
  Scotland: 17 shops (was 19, closed 2: Huntly and Keith in 2023)
  Northern_Ireland: 8 shops
  Total_Operational: 25 shops (24-26 in various sources)
  
  First_NI_Shop: Gilford (opened 1997)
  NI_Growth: From single trailer to full shop network
  NI_Coordinator_Historical: Jackie Hudson
  
RETAIL_MANAGEMENT:
  Head_of_Retail: Alan
  Appointment: 2020
  Experience: 30 years retail leadership
  Responsibilities: All 26 shops, mission-focused retail
  Philosophy: "Bringing mission to the high street"

GOODS_HANDLED:
  Collection_Methods:
    - Shop donations
    - Public donations at depots
    - Scheduled collections
    
  Item_Categories:
    - Clothing
    - Shoes
    - Furniture
    - Bric-a-brac
    - Media (books, CDs, DVDs)
    - Toys
    - Household items
    
  Processing_Locations:
    - Glasgow Depot (32 Dalziel Road, Hillington)
    - Evanton Headquarters depot
    - Individual shop back rooms

FINANCIAL_PERFORMANCE:
  BTL_Turnover_2023: £2429000
  BIL_Turnover_2023: £1120000
  Combined_Trading_Income: £3549000
  
  BTL_Donation_to_Charity:
    Year_2023: £140801
    Year_2022: £47814
    Increase: 194%
    
  Goods_Processed_BTL_2023: 2000+ tonnes
  
RECYCLING_AND_REUSE:
  Total_Donated_Goods_Reused: 2000+ tonnes
  End_Markets:
    - Retail sales (shops)
    - Wholesale (clothing, shoes)
    - Furniture sales
    - International aid (some items)
    
  Environmental_Impact:
    - Waste reduction
    - Circular economy participation
    - Member of Circular Communities Scotland
    
GIFT_AID:
  Available: Yes
  Value_Add: 25p per £1 donated
  Process: Declaration at donation

EMPLOYMENT_IMPACT:
  Shop_Staff: Majority of 143 employees
  Skills_Diversity: Various ability levels
  Inclusion: People with learning difficulties
  Volunteer_Opportunities: Extensive in shops
  
DEPOT_OPERATIONS:
  Glasgow_Depot:
    Address: 32 Dalziel Road, Hillington Park, G52 4NN
    Phone: 0141 882 0585
    Functions: Collection, processing, wholesale
    
  Evanton_Depot:
    Location: Highland Deephaven Industrial Estate
    Functions: Headquarters, warehousing, foodbank, shoebox processing
    
  NI_Operations:
    Base: 93 Templepatrick Road, Ballyclare
    Functions: NI shop support, shoebox collection

HISTORICAL_NOTES:
  1997: First NI shop opened (Gilford)
  1997: Moved to Evanton premises
  2023: Shop closures (Huntly, Keith) - consolidation strategy

================================================================================
SECTION 11: FUNDRAISING AND MARKETING
================================================================================

FUNDRAISING_STRUCTURE:
  Head_Position: Head of Fundraising & Marketing
  Historical_Leader: Danny Muschate (2007-2023)
  Staff: Fundraising team (size not specified)
  
FUNDRAISING_CHANNELS:
  Individual_Donations:
    - One-time gifts
    - Monthly recurring donations
    - Legacy giving/bequests
    - Direct mail campaigns
    
  Grant_Applications:
    - Trusts and foundations
    - Statutory grants (local government)
    - Corporate grants
    Historical_Success_Rate: 78%
    Grant_Researcher: Danny Muschate (historical)
    
  Events:
    - "Brains for Blythswood" annual quiz
    - Fundraising runs
    - Church fundraising events
    - School involvement
    - Sponsored events
    
  Gift_Catalogue:
    - Sponsor specific projects
    - Item-based giving (e.g., meals, educational support)
    - Romania project sponsorship
    - Africa project sponsorship
    - India project sponsorship
    
  Corporate_Partnerships:
    - Business sponsorships
    - Workplace giving
    - Payroll giving
    - Corporate event participation

SIGNATURE_EVENT_BRAINS_FOR_BLYTHSWOOD:
  Format: Virtual quiz
  Timing: October (regional quizzes), December (finals)
  Structure:
    - Three regional quizzes (same night)
    - Top teams from each region to finals
    - Geographically distributed teams possible
  
PROMOTIONAL_MATERIALS:
  Shoebox_Appeal:
    - Annual video production
    - Leaflets
    - Checklists
    - Impact videos
    - Direct marketing publications
    Video_Producer: Danny Muschate (historical)
    
  Social_Media:
    Facebook: 8782+ followers
    Platform_Focus: Facebook primary
    Content: Impact stories, appeals, updates
    
  Website: www.blythswood.org
  
ONLINE_FUNDRAISING_PLATFORMS:
  JustGiving: blythswood-care
  Enthuse: blythswoodcare.enthuse.com/profile
  GoFundMe: Various supporter campaigns
  
SCHOOL_ENGAGEMENT:
  Romania_Trips:
    Participants: S5 pupils from 3 Inverness schools
    Timing: August (annual)
    Purpose: Summer camp volunteer support
    Duration: Week-long
    Organizer: Danny Muschate (historical)
    Educational_Impact: Awareness of poverty, service learning
    
  Shoebox_Collection:
    - Extensive school network
    - Educational material provided
    - Assembly presentations
    - Collection points
    
CHURCH_PARTNERSHIPS:
  Shoebox_Checking: 15+ churches (example: Fullarton Centre)
  Collection_Points: Churches throughout UK
  Prayer_Support: Regular prayer partner network
  Financial_Support: Church-based donations
  Volunteer_Source: Primary volunteer recruitment
  
SUPPORTER_COMMUNICATIONS:
  Newsletter: Regular updates
  Annual_Report: Published annually
  Impact_Reporting: Stories, statistics, testimonials
  Transparency: Financial information publicly available

EXAMPLE_GRANTS_APPLIED_FOR:
  Inverness_Common_Good_Fund_2024:
    Amount: £25000
    Purpose: Highland Foodbank running costs
    Status: Recommended for approval
    Application_Date: November 2024
    
  KLM_Partnership_Grant:
    Purpose: Highland Foodbank food purchases
    Context: Addressing donation shortfalls
    
CORPORATE_SUPPORTERS_EXAMPLE:
  Collection_Partners:
    - Tesco (Inshes Inverness, Tain)
    - Asda (Inverness, Tain)
  
  Professional_Services:
    - Ledingham Chalmers (legal, deliveries)
    - KLM Partnership (financial grant)

================================================================================
SECTION 12: MISSION, VISION, VALUES, AND THEORY OF CHANGE
================================================================================

MISSION_STATEMENT:
  "To show God's love, and offer the compassion, relief and hope that can change lives for good and forever."
  
VISION_STATEMENT:
  "We seek to see people's lives being changed for good and forever as they are released from poverty, trauma and exploitation, and receive eternal life through the saving power of Jesus Christ."
  
TAGLINE: "Changing Lives For Good and Forever"
  Wordplay: "for good" = both "permanently" and "for the better"
  Spiritual_Component: "forever" = eternal life emphasis

CORE_VALUES:
  Relief_in_Crisis:
    "We bring good into times of crisis and extreme poverty through acts of kindness and the provision of immediate relief"
    
  Long_Term_Transformation:
    "We help people to change their longer-term futures for good through education and rehabilitation"
    
  Gospel_Proclamation:
    "In all our work, we seek to tell people of God's love in sending his only Son, Jesus, so that those who believe in him might not perish but have everlasting life (John 3:16)"

CHARITABLE_PURPOSES_LEGAL:
  Primary:
    - Advancement of the Christian religion
    - Relief of sickness and financial hardship
    - Promotion and preservation of good health
    - Promotion of education (particularly understanding of Christian religion)
    - Printing, publishing, production and distribution of Christian literature
  
OPERATIONAL_VALUES:
  Integrity_and_Compassion:
    "We aim to serve the physical, emotional and spiritual needs of others with integrity and compassion, at home and abroad"
    
  Excellence:
    "We strive for excellence in all that we do, giving opportunity to people with different levels of ability and treating each individual with respect, regardless of background or belief"
    
  People_Centered:
    "We value our people, both staff and volunteers, and believe they deserve an equitable and motivating working environment which expresses care for people"
    
  Sustainability_and_Stewardship:
    "We are committed to care responsibly for God's creation and to aim for sustainability in the projects we initiate and develop"

MISSION_DELIVERY_PILLARS:
  Education:
    "Education projects offer opportunities for children and young people (and particularly the disadvantaged) to realise their potential"
    Examples: Talita Kum, Sargy, Cornerstone, literacy programs
    
  Community_Action:
    "Community action provides people of all ages with sustainable and transformational life-changing opportunities, especially in areas of deprivation"
    Examples: Foodbanks, Daniel Centre, Basis project, charity shops
    
  Gospel_Teaching:
    "Christian ministry and literature distribution enable effective sharing of the life-changing gospel message of Jesus Christ, bringing hope and purpose to those we serve"
    Examples: Shoebox literature, Bible distribution, Christianity Explored, seafarers' ministry

THEORY_OF_CHANGE:
  Immediate_Relief:
    Input: Shoeboxes, food packages, emergency aid
    Output: Crisis needs met
    Outcome: Hope, dignity restored
    
  Education_and_Development:
    Input: Tutoring, meals, supplies, training
    Output: School attendance, skill acquisition
    Outcome: Future opportunities, employment, independence
    
  Spiritual_Transformation:
    Input: Christian literature, gospel teaching, discipleship
    Output: Exposure to Christian message
    Outcome: Eternal life, lasting purpose
    
  Sustainability_Approach:
    - Local leadership in all international projects
    - Self-sufficiency goals
    - Partnership model (not dependency)
    - Evaluation toward independence
    - Solid financial base establishment

FOUNDER'S_PHILOSOPHY:
  Founder: Rev Jackie Ross
  Core_Insight: "Agencies like Blythswood can go directly to the people in need. Sometimes governments can make improvements with hospitals and schools, but these can take 5-10 years to happen. Blythswood, and agencies like us, can help people sometimes within a week and keep on helping them until we're not needed."
  
  Biblical_Foundation: Faith-based approach to provision
  Reserves_Philosophy: "Not appropriate to retain significant surpluses" - trust in God's provision
  
HERITAGE_AND_CONTINUITY:
  Founded: 1966 (58 years)
  Generations:
    First: Rev Jackie Ross (1966-2002)
    Second: James Campbell (1998-2024)
    Third: Jeremy Ross (2024-present)
  
  Continuity_Themes:
    - Christian conviction (salvation through Jesus)
    - Practical compassion
    - Direct aid to individuals
    - Partnership with churches
    - Literature distribution
    - International and domestic work
    
  Adaptation_Philosophy:
    "Operating in a changing world, our organisation must always embrace change. The challenge for those of us who have now assumed leadership is to continue to help the poorest with the same Christian compassion shown by those who went before." - Jeremy Ross, 2023

================================================================================
SECTION 13: IMPACT DATA AND OUTCOMES
================================================================================

AGGREGATE_LIFETIME_IMPACT:
  Shoebox_Recipients: 2739772 (since 1993)
  Foodbank_Beneficiaries_UK: 70000+ (since 2005)
  Countries_Served: 21+
  Years_Operating: 58+ (since 1966)
  
ANNUAL_IMPACT_2023:
  Shoeboxes_Distributed: 84655 - 89000 (sources vary)
  Foodbank_Users_UK: 10194 people
  Food_Distributed_UK: 103.7 tonnes
  Christian_Literature_Items: 123500
  Volunteer_Hours: 30000+
  Goods_Recycled: 2000+ tonnes
  Romania_Children_Supported:
    Talita_Kum: 70+ children
    Daniel_Centre: 5-7 young men
    Basis_Project: 30 families
  India_Children: 25
  Kenya_Children: 350
  
OUTCOMES_DOCUMENTED:
  Education:
    - Children catching up grade levels (1 year in 2 months example)
    - Homework completion despite family challenges
    - University aspirations developed
    - School dropout prevention
    - Literacy achievement
    
  Employment:
    - Daniel Centre residents gaining jobs
    - Independent living achieved
    - Financial management skills developed
    - English proficiency (6 months example)
    
  Health:
    - Malnutrition recovery (India)
    - Regular meals provision
    - Mental health support
    - Hygiene access
    
  Social:
    - Family preservation (vs. orphanage placement)
    - Modern slavery escape and recovery
    - Addiction recovery (Hungary)
    - Prevention of premature marriage
    - Reduction in juvenile delinquency
    
  Spiritual:
    - Gospel exposure through literature (100000+ annually)
    - Discipleship programs
    - Faith development (Christianity Explored: 264 participants)
    - Church growth support
    
QUALITATIVE_IMPACT_EXAMPLES:
  Foodbank_Client: "I'm blown away that everyone here is so nice, and the food you've given me is such a help. I can't thank you enough."
  
  Ukraine_Parent: "After all that has happened in the past year, they are just happy to be alive."
  
  Romania_Teacher: "Attending Blythswood does Maria good." (regarding trauma recovery)
  
  Serbia_Participant: "The more we get to know Christianity, the more we get to know God and his will for us."
  
  Romania_Camp_Impact: "For children like Maria the chance to go away from home for a few days is a unique opportunity to grow as a person."

EFFICIENCY_METRICS:
  Cost_Per_Shoebox_Literature: £0.41
  Administrative_Overhead: 4%
  Volunteer_Economic_Value: £310000+ annually
  Support_Costs_Percentage: 2.16%
  
REACH_AND_SCALE:
  Geographic_Reach: Europe, Africa, Asia, UK
  Partner_Organizations: Hundreds (churches, agencies, NGOs)
  Referral_Agencies_UK: 100+ (foodbank referrals)
  Collection_Points: Extensive (churches, supermarkets, shops)

SUSTAINABILITY_INDICATORS:
  Daniel_Centre:
    - Residents transition to independent living
    - After-care community maintained
    - Social housing placements
    - Sustained employment
    
  Talita_Kum:
    - Daily attendance
    - Parental engagement
    - Community recognition
    - Government funding complement (not replacement)
    
  Foodbanks:
    - CAB advisor early intervention reducing demand
    - Partnership with 100+ referral agencies
    - Sustainable food supply chains
    
  Romania_General:
    - Local leadership (Balazs Csiszer, Adrian Popa)
    - 20+ year project track records
    - Self-sufficiency orientation

================================================================================
SECTION 14: PARTNERSHIPS AND NETWORKS
================================================================================

STATUTORY_PARTNERS:
  Highland_Council:
    - Care Health and Social Care Service
    - Service Points
    - Housing Services
    - Common Good Fund (grant funder)
    
  Scottish_Welfare_Fund: Foodbank referrals
  
  NHS_Highland: Historical employment connection (Danny Muschate)

NATIONAL_PARTNERS:
  Trussell_Trust:
    Relationship: Foodbank franchise/partnership
    Duration: Since 2005
    Additional_Funding: CAB advisor support
    
  Christian_Focus_Publications:
    Collaboration: Shoebox literature production
    Type: Co-publishing
    
  Trinitarian_Bible_Society:
    Collaboration: Adult calendar for shoeboxes
    
  SERA_Scottish_Emergency_Relief_Agency:
    Collaboration: Fire equipment to Ukraine
    Volume: Majority of 168 tonnes (2023)
    
  Edinburgh_Dog_and_Cat_Home:
    Collaboration: Pet food for foodbank clients

CHARITY_SECTOR_MEMBERSHIPS:
  Circular_Communities_Scotland_CCS: Recycling and reuse
  Charity_Retail_Association_CRA: Shop operations
  
BUSINESS_PARTNERS:
  Tesco: Permanent foodbank collection points (2 locations)
  Asda: Permanent foodbank collection points (2 locations)
  Ledingham_Chalmers: Legal services, deliveries to foodbank
  KLM_Partnership: Financial grant support
  10ofthose.com: Christian book supplier

CHURCH_PARTNERSHIPS:
  Free_North_Church_Inverness: Madras Street Mission Hall (foodbank historical venue)
  Castle_Street_Church: Mission partnership, Romania project support
  Invergordon_Parish_Church: Seafarers' Centre hosting
  Greyfriars_Free_Church: Romania camp volunteers
  15+_Churches: Shoebox checking (Fullarton Centre example)
  Hundreds_of_Churches: Collection points, prayer support, donations
  
  Church_Types_Served:
    - Free Church of Scotland
    - Baptist
    - Pentecostal
    - Evangelical
    - Reformed
    - Presbyterian
    - Interdenominational cooperation

INTERNATIONAL_PARTNERS_ROMANIA:
  Reformed_Pastor_Levente_Horvath: Historical founding connection (1980s)
  Local_Church_Networks: Established pre-1989
  Children_for_Christ: Summer camp partnership
  
INTERNATIONAL_PARTNERS_INDIA:
  Cornerstone_Trust: Primary partner (Asmita Vadavana)
  India_Bible_Literature: Book recipient
  
INTERNATIONAL_PARTNERS_KENYA:
  Sargy_Education_Centre: Primary partner (Samwel Okomo)
  
INTERNATIONAL_PARTNERS_HUNGARY:
  Bonus_Pastor_Foundation: Addiction recovery (since 1993)
  
INTERNATIONAL_PARTNERS_SERBIA:
  David_Armus: Coordinator
  Baptist_Churches: Christianity Explored distribution
  Pentecostal_Churches: Christianity Explored distribution
  Evangelical_Roma_Churches: Christianity Explored distribution
  
INTERNATIONAL_PARTNERS_KOSOVO:
  Faton_Barisha: Distribution coordinator (Gjakova area)
  
INTERNATIONAL_PARTNERS_UKRAINE:
  Olga: Coordinator (based Cluj, Romania)
  Multiple_Church_Partners: Aid distribution
  Note: Some partners ended due to other funding with less accountability
  
INTERNATIONAL_PARTNERS_MOLDOVA:
  Children_for_Christ: Summer camps
  
VOLUNTEER_GROUPS:
  Go_Relief: Northern Ireland renovation team (Daniel Centre 2018)
  Suits_on_Bikes: Charity cycling fundraiser (Talita Kum support)
  Inverness_School_Groups: S5 pupils (3 schools)
  
PROFESSIONAL_SERVICES:
  Audit: Annual accounts audited
  Legal: Ledingham Chalmers
  Banking: Not specified
  
SUPPORTER_GROUPS:
  Prayer_Partners: Network throughout UK
  Regular_Donors: Individual supporters
  Legacy_Donors: Will bequests
  Corporate_Donors: Business supporters
  Trusts_and_Foundations: Grant funders

================================================================================
SECTION 15: FACILITIES AND INFRASTRUCTURE
================================================================================

HEADQUARTERS_EVANTON:
  Address: Highland Deephaven Industrial Estate, Evanton, IV16 9XJ
  Moved_To_Site: 1997
  
  Functions:
    - Administrative offices
    - Warehouse and depot
    - Shoebox processing
    - Donated goods sorting
    - Vehicle maintenance
    - Staff employment hub (90 Highland staff)
    
GLASGOW_DEPOT:
  Address: 32 Dalziel Road, Hillington Park, Glasgow, G52 4NN
  
  Functions:
    - Collection point
    - Goods processing
    - Wholesale operations
    - Volunteer hub
    - Distribution centre
    
NORTHERN_IRELAND_OFFICE:
  Address: 93 Templepatrick Road, Ballyclare, BT39 9RQ
  
  Functions:
    - NI operations coordination
    - Shop support
    - Shoebox collection
    
FOODBANK_CENTRE_INVERNESS:
  Address: 1 Glebe Street, Inverness, IV1 1RF
  Moved_To_Site: Date not specified (consolidated operations)
  
  Features:
    - Dedicated foodbank entrance (privacy)
    - Private meeting room
    - Storage space
    - Receiving and sorting areas
    - Shared building with charity shop
    - Wheelchair accessible
    - On-site parking
    - Ramp entrance
    
  Operating_Hours_Collection: Monday-Friday 12:00-14:00
  Operating_Hours_Office: Monday-Friday 09:00-15:00
  
  Historical_Location: Madras Street Mission Hall (Free North Church)
  
CHARITY_SHOPS_SCOTLAND:
  Total: 17 (was 19 in 2023)
  Closures_2023: Huntly, Keith
  
  Example_Locations:
    - Inverness (Glebe Street)
    - Glasgow area
    - Other Highland locations
    
CHARITY_SHOPS_NORTHERN_IRELAND:
  Total: 8
  First_Shop: Gilford (1997)
  Growth_Pattern: Single trailer → full network
  
ROMANIA_FACILITIES:
  Daniel_Centre_Cluj:
    Opened: 2000
    Renovated: 2018 (Go Relief team)
    Configuration: Self-contained studio flats
    Capacity: 5-7 residents
    Features: Individual kitchens, living spaces
    
  Talita_Kum_Jimbolia:
    Opened: 2001
    Facility_Type: After-school centre
    Features: Meal preparation, shower facilities, teaching spaces
    New_Building: Funded via European Regional Development Fund
    Capacity: 70+ children (TK1, TK2, TK3)
    
  Cluj_Depot:
    Status: Sale in process (not completed 2024)
    Function: Historical distribution centre
    
  Rental_Apartments:
    Purpose: Daniel Centre graduate housing
    Status: Ongoing, some vacancies
    
INDIA_FACILITIES:
  Beacon_Centre_Turbe:
    Opened: December 2022
    Features: Culinary training, sports, toddlers' groups, garden
    Future: Child development centre (Shramik Nagar)
    
  Cornerstone_Day_Centre:
    Location: Navi Mumbai
    Capacity: 20 children
    
KENYA_FACILITIES:
  Sargy_Education_Centre:
    Location: Rusinga Island
    Capacity: 350 children
    Features: School, meal preparation
    
VEHICLES_AND_LOGISTICS:
  Trucks: Multiple (for international aid delivery)
  Distribution_Historical: Average 1+ truckload per week (1990)
  2023_Deliveries: 322 tonnes total aid
  
INFORMATION_TECHNOLOGY:
  Website: www.blythswood.org
  Online_Giving: Multiple platforms
  Social_Media: Facebook primary
  Email_System: Multiple departmental addresses
  
STORAGE_CAPACITY:
  Evanton: Large warehouse
  Glasgow: Depot facilities
  Foodbank: Dedicated storage (Inverness and network)
  Shop_Storage: Individual shop back rooms

================================================================================
SECTION 16: HISTORICAL MILESTONES AND TIMELINE
================================================================================

1966: Founding
  - Blythswood Tract Society founded in Glasgow
  - Four trainee ministers: Rev Jackie Ross, Donald Ross, Ian Tallach, John Tallach
  - Office near Blythswood Square
  - Street evangelism, homeless hostel visits
  
1970: Ministers dispersed to congregations outside Glasgow

1977: Relocation to Lochcarron
  - Jackie Ross serving as minister in Lochcarron, Wester Ross
  
1970s: Bible printing and distribution
  - 20000 Bibles per printing run
  - Distribution: Africa, India, Eastern Bloc, UK schools, prisons
  - Christian bookshops established (Scotland, England, NI)
  - Book vans and agencies
  
1980s: International aid begins
  1984: Emergency aid to Poland (first major international response)
  1988: Armenia earthquake response
  1989: Fall of communism - immediate access to Eastern Europe
  1980s: Jackie Ross visits Romania, meets Levente Horvath
  
1990: Major expansion
  - 1+ truckload per week to Eastern Europe
  - Church networks enable rapid response
  
1993: Shoebox Appeal launched
  - Becomes flagship program
  
1995: Blythswood Romania founded
  - Christian charity established
  - Hundreds of trucks: Inverness to Romania route
  
1997: Infrastructure expansion
  - Moved to Evanton premises (warehouse and offices)
  - First Northern Ireland shop opened (Gilford)
  
1998: James Campbell joins as staff
  - Later becomes Chief Executive
  - Jeremy Ross works as fundraiser/area coordinator
  
2000: Daniel Centre opened
  - Cluj, Romania
  - First owned international project
  - Residential care for ex-orphanage young men
  - Founder Jackie Ross inaugurates
  
2001: Talita Kum launched
  - Jimbolia, Romania
  - After-school program for disadvantaged children
  
2002: Founder Rev Jackie Ross passed away
  - Legacy continues
  - Vision maintained
  
2005: Foodbank partnership
  - Began running foodbanks with Trussell Trust
  
2007: Danny Muschate joins
  - Head of Fundraising & Marketing
  - From NHS Highland (9 years)
  
2009: Paul Macleod joins
  - Chief Operating Officer
  - From private sector
  
2018: Daniel Centre renovation
  - Self-contained studio flats
  - Go Relief volunteer team (Northern Ireland)
  
2020: Alan joins as Head of Retail
  - 30 years retail experience
  - 26 shop network oversight
  
2021: Jeremy Ross joins board
  - Trustee appointment (February)
  - Blythswood Ireland consolidated into accounts (January)
  
2022: Ukraine Emergency Appeal
  - Raised £735000+
  - Ongoing crisis response
  - SERA partnership (fire equipment)
  - Peak income year: £10.4 million
  
2022: Beacon Centre opened (December)
  - Turbe, Navi Mumbai
  - Cornerstone Trust expansion
  
2023: Leadership transition
  - Jeremy Ross appointed Chief Executive (February 1)
  - James Campbell retired (January 31, 26 years service)
  - Finlay Mackenzie retired (30 years service)
  - Danny Muschate retired (October, 16 years service)
  - Carole Gordon (trustee) died (October 8)
  - Shop closures: Huntly and Keith
  - Shoebox Appeal 31st anniversary
  
2024: Continued operations
  - Highland Foodbank 20th anniversary (2005-2025)
  - New governance structure in process (foodbank)
  - Common Good Fund application (£25000)
  - Projected deficit: First in recorded history
  - New trustees appointed (Nathan Hawthorne, others)
  
2025: Current status
  - 58 years of operation
  - Second-generation leadership (Jeremy Ross)
  - Strategic planning for sustainability
  - Maintaining 21+ country reach

ORGANIZATIONAL_RESTRUCTURING:
  1966-1993: Blythswood Tract Society
  1993: Blythswood Care 1993 (trust deed, SC021848)
  2018: Blythswood Care (SCIO, SC048001)
  Note: Predecessor entity maintains legal title to some retail properties

================================================================================
SECTION 17: CHALLENGES, RISKS, AND OPPORTUNITIES
================================================================================

CURRENT_CHALLENGES:
  Financial:
    - Income decline: -19.4% from 2022 peak to 2024 projected
    - First projected deficit: -£139255 (2024)
    - Rising foodbank operational costs
    - Cost of living crisis impact on donations
    - Inflation affecting all operations
    - Shop closures (Huntly, Keith) indicating retail pressure
    
  Operational:
    - Ukraine crisis ongoing (medium-term planning needed)
    - Increased foodbank demand despite economic indicators
    - Romania project sustainability (Cluj depot sale delays)
    - Staffing challenges (Romania teacher salaries, retention)
    - Leadership transition integration (new CE, COO continuity)
    - Northern Ireland governance establishment
    
  External:
    - Regulatory environment (OSCR trustee information requirements 2026)
    - Competition for donor funds
    - Changing retail landscape (charity shops)
    - Post-pandemic economic uncertainty
    - Political instability (Ukraine, Eastern Europe)
    
RISK_MANAGEMENT_APPROACH:
  Process:
    - Formal risk identification
    - Prioritization by impact and likelihood
    - Mitigation strategy development
    - Quarterly Board monitoring
    - Bi-annual full review
    
  Major_Financial_Risk:
    Identified: Financial sustainability (charity and trading subsidiary)
    Mitigation:
      - Regular liquid funds review
      - Bank liaison
      - Active trade debtor/creditor management
      - Working capital monitoring
      
  Non_Financial_Risks:
    Fire_Safety: Robust policies, regular training
    Health_and_Safety: All facilities, quarterly incident reports to Board
    Operational_Continuity: Backup systems, procedures
    
OPPORTUNITIES:
  Strengths_to_Leverage:
    - Strong heritage and brand (58+ years)
    - Second-generation leadership bringing fresh energy
    - Extensive volunteer network (1000+)
    - Proven grant success rate (78%)
    - Multiple income streams (diversification)
    - Established international partnerships
    - 26 charity shops (earned income base)
    - Low overhead costs (4%)
    - Strong reserves position (£2.64M net assets)
    
  Growth_Areas:
    Individual_Donors:
      - "Sponsor a Smile" type programs
      - Legacy giving expansion
      - Monthly giving growth
      - Digital fundraising expansion
      
    Corporate_Partnerships:
      - Sponsorship opportunities
      - Workplace giving
      - Corporate social responsibility alignment
      - Product donation partnerships
      
    Grant_Funding:
      - Statutory grants (more local government)
      - European funding (Romania projects)
      - Foundation grants (untapped foundations)
      - Corporate foundation grants
      
    Earned_Income:
      - Online sales development (planned)
      - Shop optimization
      - Wholesale expansion
      - Social enterprise models
      
    Program_Expansion:
      - Talita Kum vocational training (20th anniversary development)
      - Beacon Centre child development centre (Shramik Nagar)
      - Foodbank network optimization
      - New project countries (evaluation basis)
      
  Marketing_and_Awareness:
    - Social media expansion (beyond Facebook)
    - Direct mail optimization
    - Story-telling and impact reporting
    - Video content (successful shoebox videos)
    - Influencer partnerships
    - Press and media relations
    
STRATEGIC_PRIORITIES_STATED:
  Immediate:
    - Maintaining financial sustainability
    - Controlling foodbank costs while meeting demand
    - Ukraine support continuation
    - Shoebox appeal growth
    
  Medium_Term:
    - Developing next generation volunteers and donors
    - Strengthening retail operations
    - Expanding Romania education programs
    - UK mission review (foodbanks, literature, charity shops)
    
  Long_Term:
    - Self-sufficiency for international projects
    - Sustainable funding beyond short-term grants
    - Leadership pipeline development
    - Strategic geographic expansion (evaluated)

FUTURE_PLANS_DOCUMENTED:
  Romania:
    - Talita Kum extension: vocational training, further education support (2024)
    - Beacon Centre development: culinary, sports, career guidance
    - New child development centre: Shramik Nagar
    - Turbe after-school program: expansion through Beacon Centre
    
  Ukraine:
    - Medium-term plan development
    - Continued crisis response
    - Partner evaluation
    - Practical aid and funding balance
    
  UK:
    - Foodbank mission review
    - Christian literature strategy review
    - Charity shop utilization review
    - New governance for Highland Foodbank
    
  International:
    - Regular partner evaluation (13 countries)
    - Self-sufficiency and sustainability assessment
    - New country consideration (evaluated basis)
    - Literature distribution expansion (8 additional countries)

RESERVES_POLICY:
  Philosophy: "Not appropriate to retain significant surpluses"
  Basis: Christian faith in God's provision
  Target: Sufficient for working capital and ongoing activities
  Current_Position: £2.64M net assets (adequate for policy)
  Board_Review: Regular monitoring

POST_BALANCE_SHEET_CONSIDERATIONS:
  Year_2023_Statement: No material changes to operating activities
  No_Events_Requiring_Disclosure: Between 2023-12-31 and report date
  FRS102_Compliance: Directors concluded accurate and fair view

================================================================================
SECTION 18: GRANT APPLICATION RELEVANT INFORMATION
================================================================================

FUNDING_NEEDS_CATEGORIZED:

Core_Operating_Support:
  Foodbank_Operations:
    Annual_Need_Inverness: ~£50000-75000 (estimated from £25K grant request)
    Justification: Rising costs, cost of living crisis
    Current_Funding: Donations, Trussell Trust support, statutory grants
    Gap: Growing expenses vs. relatively stable income
    
  Literature_Production:
    Annual_Spend_2023: £50300 (shoebox literature)
    Per_Unit_Cost: £0.41
    Scale: 123500 items annually
    Languages: 6
    Funding_Sources: Donations, designated funds
    
  UK_Staff_Salaries:
    Total_Staff: 143
    Primary_Location: Highland (90 staff)
    Current_Funding: Trading income, donations, grants
    
  International_Project_Support:
    Romania_Annual: Estimated €50000+ (Talita Kum example)
    Distribution: Daniel Centre, Talita Kum, Basis, others
    Current_Funding: Gift catalogue, donations, grants
    
Capital_Projects:
  Facility_Improvements:
    Priority: Foodbank expansion/optimization
    Priority: Shop refurbishments
    Priority: Warehouse efficiency
    
  Romania_Infrastructure:
    TK_Vocational_Training_Facilities: Planned expansion
    Beacon_Centre_Development: Child development centre
    Daniel_Centre_Maintenance: Ongoing
    
  Vehicle_Replacement:
    Need: Delivery vehicles, trucks
    Current_Fleet: Multiple vehicles (age not specified)
    
Program_Expansion:
  Talita_Kum_Vocational:
    Timeline: 2024 onwards (20th anniversary)
    Need: Equipment, instructor salaries, materials
    Beneficiaries: TK3 (high school students), TK2 graduates
    
  India_Child_Development_Centre:
    Location: Shramik Nagar
    Partner: Cornerstone Trust
    Status: Planned
    Model: Based on Beacon Centre success
    
  Foodbank_Rural_Network:
    Current: 9 Highland locations
    Opportunity: Additional rural areas
    Requirement: Local partnerships, storage, volunteers
    
Emergency_Response:
  Ukraine_Ongoing:
    Annual_Need: Variable (£735K raised 2022)
    Type: Practical aid, emergency equipment, financial support
    Partners: Multiple Ukrainian organizations
    Timeline: Medium-term (ongoing conflict)
    
  Future_Crisis_Capacity:
    Track_Record: Rapid response (Poland 1984, Armenia 1988, Ukraine 2022)
    Infrastructure: Logistics capability, partner networks
    Flexibility: Ability to pivot resources
    
Restricted_Funding_Opportunities:
  Shoebox_Appeal:
    Annual_Scale: 85000-90000 boxes
    Funding_Need: £3 per box minimum (£255000-270000)
    Current: Individual donations
    Opportunity: Corporate sponsorship, bulk donations
    
  Specific_Country_Projects:
    Romania: Education, residential care
    India: Foster care, day programmes
    Kenya: School meals, education
    Ukraine: Emergency relief
    Serbia: Christian literature
    Hungary: Addiction recovery support
    
  Foodbank_Specific:
    Food_Purchase: When donations insufficient
    Delivery_Service: Expanding for vulnerable clients
    CAB_Advisor: Continuation funding (currently Trussell Trust)
    
GRANT_READY_INFORMATION:

Organizational_Capacity:
  Track_Record: 58 years operational
  Financial_Health: Strong despite recent challenges
  Governance: Professional Board, clear structure
  Monitoring_and_Evaluation: Project evaluation, OSCR compliance
  Reporting: Annual reports, impact stories, financial transparency
  
Geographic_Reach:
  UK_Coverage: Scotland, Northern Ireland, England (donors)
  International: 21+ countries, 13 with active partnerships
  Rural_Focus: Highland Scotland, Romanian rural areas, Kenyan island
  Urban_Focus: Glasgow, Edinburgh, Mumbai, Cluj
  
Beneficiary_Demographics:
  Age_Range: Infants to elderly
  Vulnerable_Groups:
    - Children in poverty
    - Care leavers
    - Low-income families
    - Refugees/IDPs (Ukraine)
    - Homeless and at-risk
    - Benefit recipients
    - Addiction recovery
    - Mental health challenges
    - Domestic violence survivors
    - Ethnic minorities (Roma)
    
  Scale_Annual: 100000+ direct beneficiaries (estimated)
  
Impact_Measurement:
  Quantitative:
    - Number of boxes distributed
    - Tonnes of food provided
    - Number of people fed
    - Children in education programs
    - Young men in residential care
    - Items of literature distributed
    - Volunteer hours
    - Tonnes recycled
    
  Qualitative:
    - Client testimonials
    - School progress reports
    - Employment outcomes
    - Independent living achievement
    - Spiritual transformation stories
    - Community feedback
    - Partner assessments
    
Partnership_Approach:
  Model: Local leadership, capacity building
  Duration: Long-term (20+ years some projects)
  Support_Type: Financial, material, training, oversight
  Evaluation: Regular review, self-sufficiency goals
  Transparency: High accountability standards
  
Value_for_Money:
  Administrative_Overhead: 4% (exceptionally low)
  Volunteer_Multiplier: 10:1 volunteer to staff ratio
  Literature_Cost: £0.41 per item
  Leveraging: Donated goods, volunteer time, partner co-funding
  
Alignment_with_Funder_Priorities:
  Poverty_Alleviation: Core mission
  Education: Major program pillar
  Child_Welfare: Priority populations
  Community_Development: Embedded approach
  Emergency_Response: Proven capability
  Faith_Based: Explicit Christian foundation
  Sustainability: Project design principle
  Rural_Development: Geographic focus areas
  Social_Enterprise: Charity shop model
  Volunteer_Engagement: Extensive network
  
Restricted_Fund_Management:
  Capability: Yes, demonstrated with Ukraine appeal
  Reporting: Project-specific outcomes
  Transparency: Financial breakdown by project area
  Audit: Annual audit process

================================================================================
SECTION 19: CONTACT INFORMATION BY FUNCTION
================================================================================

General_Enquiries:
  Phone: 01349 830 777
  Email: info@blythswood.org
  Address: Highland Deephaven, Evanton, IV16 9XJ
  
Chief_Executive:
  Name: Jeremy Ross
  Contact_Route: Via main office
  
Fundraising_and_Grants:
  Email: fundraising@blythswood.org
  Historical_Contact: Danny Muschate (retired 2023)
  
Foodbank_Highland:
  Phone: 01463 717 630
  Email: foodbank@blythswood.org
  Email_Admin: foodbank.admin@blythswood.org
  Address: 1 Glebe Street, Inverness, IV1 1RF
  Manager: Lorna Dempster
  
Foodbank_Edinburgh:
  Contact: Via main office
  Manager: Miriam Montgomery
  
Glasgow_Depot:
  Phone: 0141 882 0585
  Email: glasgowdepot@blythswood.org
  Address: 32 Dalziel Road, Hillington Park, G52 4NN
  
Northern_Ireland:
  Phone: 028 93 349 859
  Email: enquiries.ireland@blythswood.org
  Address: 93 Templepatrick Road, Ballyclare, BT39 9RQ
  
Retail_Operations:
  Contact: Via main office
  Head_of_Retail: Alan
  
Romania_Operations:
  Contact: Via main office
  Executive_Director: Balazs Csiszer (Cluj)
  Talita_Kum_Director: Adrian Popa (Jimbolia)
  
Press_and_Media:
  Contact_Route: Via main office or fundraising@blythswood.org
  
Volunteer_Enquiries:
  Contact_Route: Via main office or specific location
  
Shoebox_Appeal:
  Contact_Route: Via main office
  Website: www.blythswood.org (appeal information)
  
Donations_and_Legacies:
  Contact_Route: Via main office
  Online: Multiple platforms (JustGiving, Enthuse, website)
  
Shop_Donations:
  Contact: Any Blythswood charity shop
  Glasgow_Depot: 0141 882 0585
  
================================================================================
SECTION 20: MEDIA AND PROMOTIONAL RESOURCES
================================================================================

Website: www.blythswood.org
  Features:
    - Donation portal
    - Shoebox appeal information
    - Foodbank locations
    - Impact stories
    - Gift catalogue
    - Event information
    - Volunteer opportunities
    
Social_Media:
  Facebook:
    Page: Blythswood Care
    Followers: 8782+ (as of 2023)
    Tagline: "Changing Lives For Good and Forever"
    Location_Tag: Evanton
    Activity: Regular posts (217 talking about this)
    Visits: 193 check-ins
    
Fundraising_Platforms:
  JustGiving: blythswood-care
  Enthuse: blythswoodcare.enthuse.com/profile
  GoFundMe: Various supporter campaigns
  
Annual_Report:
  Format: PDF
  Availability: OSCR website, direct request
  Latest: 2023 (published August 2024)
  Content: Financial statements, impact stories, program updates
  
Promotional_Materials:
  Shoebox_Appeal:
    - Leaflets and checklists
    - Annual video
    - Posters
    - School assembly materials
    - Church presentation materials
    
  Gift_Catalogue:
    - Printed and online
    - Item-specific giving options
    - Impact descriptions
    - Pricing information
    
Video_Content:
  Annual_Shoebox_Video:
    Producer: Danny Muschate (historical)
    Purpose: Impact demonstration, donor engagement
    Distribution: Website, social media, presentations
    
Images:
  Availability: Annual report, website, social media
  Content: Beneficiaries, projects, volunteers, facilities
  Usage: Donor communications, grant applications, press
  
Press_Coverage_Recent:
  Highland_Foodbank_Grant: Inverness Courier (3 days before November 19, 2025)
  Press_&_Journal: Various coverage
  Ross-shire_Journal: Local coverage
  Northern_Scot: Regional coverage
  
Historical_Articles:
  Banner_of_Truth: Founder profile
  Church_publications: Mission partnerships
  
OSCR_Registration_Logo:
  Availability: Free download
  Usage: Website, email signatures, publications
  Purpose: Credibility, transparency
  
Branding:
  Tagline: "Changing Lives For Good and Forever"
  Color_Scheme: Not specified in sources
  Logo: Available (OSCR registration version)
  
Speaking_Engagements:
  Availability: Staff and volunteers give talks
  Audiences: Churches, schools, community groups
  Contact: Via main office

================================================================================
SECTION 21: LEGAL AND COMPLIANCE FRAMEWORK
================================================================================

Regulatory_Authority:
  Primary: Office of the Scottish Charity Regulator (OSCR)
  Secondary: Companies House (company registration)
  Northern_Ireland: Charity Commission for Northern Ireland (BIL)
  
Charity_Registration:
  Scotland_Primary: SC048001 (Blythswood Care SCIO)
  Scotland_Predecessor: SC021848 (Blythswood Care 1993)
  Northern_Ireland: NIC104515 (Blythswood Ireland Limited)
  
Company_Registration:
  Scotland: SC583493 (Blythswood Care)
  Northern_Ireland: NI050683 (Blythswood Ireland Limited)
  England: SC583493 (trading subsidiary - verify)
  
Legal_Structure_Primary:
  Type: Scottish Charitable Incorporated Organisation (SCIO)
  Act: Charities and Trustee Investment (Scotland) Act 2005
  Governing_Document: Constitution (SCIO)
  Liability: Limited
  
Legal_Structure_Subsidiaries:
  BTL: Company limited by guarantee (wholly owned)
  BIL: Company limited by guarantee (sole member)
  
Charitable_Purposes_Legal:
  Registered_Under:
    - Advancement of religion
    - Relief of poverty
    - Advancement of education
    - Relief of sickness
    - Promotion of health
  
Regulatory_Filings:
  OSCR_Annual_Return: Due annually, filed on time
  Companies_House_Confirmation_Statement: Filed December 2024
  Accounts_Submission: Annual to OSCR and Companies House
  Trustee_Information: New requirement from June 2025 (published Jan 2026)
  
Governance_Documents:
  Constitution: SCIO constitution
  Articles_of_Association: Historical (1993 entity)
  Trustee_Powers: Defined in constitution
  Appointment_Process: Special resolution by guarantors
  
Financial_Regulations:
  Accounting_Standard: FRS102
  Audit_Requirement: Yes (annual)
  Independent_Examination: N/A (audited)
  Financial_Year_End: December 31
  
Public_Benefit_Requirement:
  OSCR_Objective: Promote public benefit understanding
  Demonstration: Annual report public benefit statement
  Geographic_Scope: Scotland, NI, international
  Beneficiary_Access: Open referral system (foodbanks), general public (shops)
  
Data_Protection:
  GDPR_Compliance: Required
  Client_Privacy: Emphasized (foodbank separate entrance)
  Donor_Records: Maintained
  Gift_Aid_Records: Required
  
Health_and_Safety:
  Policy: Robust policies in place
  Training: Regular awareness training
  Incident_Reporting: Quarterly to Board
  Facilities: All operational sites covered
  
Insurance:
  Types_Likely:
    - Public liability
    - Employer's liability
    - Professional indemnity
    - Buildings and contents
    - Vehicle fleet
    - Trustee indemnity
  (Specific coverage not detailed in sources)
  
Employment_Law:
  Employees: 143 total
  Jurisdiction: Scottish employment law (primary)
  Fair_Work: Committed to equitable environment
  Living_Wage: Volunteer value calculation uses National Living Wage
  
Fundraising_Regulation:
  Self_Regulation: Charity sector standards
  Transparency: Financial information public
  Donor_Rights: Thanking, reporting, choice
  
International_Operations:
  Romania_Legal_Entity: Blythswood Romania (established 1995)
  Local_Compliance: Romanian charity law
  Partnership_Agreements: With local organizations
  Financial_Transfers: International aid regulations
  
Trading_Regulations:
  Trading_Subsidiary: BTL separate entity for VAT/tax purposes
  Gift_Aid: Available on donated goods
  Retail_Regulations: Consumer protection, health & safety
  Waste_Regulations: Recycling compliance
  
Taxation:
  Charitable_Tax_Exemption: Yes
  Gift_Aid_Relief: 25p per £1
  Trading_Income: Via subsidiary
  VAT_Status: Not specified (likely exempt/zero-rated activities)
  
Transparency:
  Public_Documents:
    - Annual accounts (OSCR)
    - Trustee report (OSCR)
    - Constitutional documents
    - Company filings
  Website_Disclosure: Contact info, mission, activities
  
Complaints_Procedure:
  Internal: Policies in place (assumed standard)
  OSCR_Route: Available for public concerns
  
Fundraising_Standards:
  Approach: Ethical, transparent
  Vulnerable_Persons: Appropriate safeguarding
  Marketing: Truthful, not manipulative

================================================================================
SECTION 22: GLOSSARY AND DEFINITIONS
================================================================================

SCIO: Scottish Charitable Incorporated Organisation
  - Legal form for Scottish charities
  - Incorporated but not a company
  - Limited liability for trustees
  - Registered with OSCR
  
OSCR: Office of the Scottish Charity Regulator
  - Independent regulator
  - Maintains Scottish Charity Register
  - Ensures charitable status compliance
  
Trussell_Trust: National foodbank network
  - Franchise/partnership model
  - Standards and support provider
  - Founded 2000s
  
Gift_in_Kind: Non-monetary donations
  - Donated goods for shops
  - Accounted at fair value
  - Major income component (40% of revenue)
  
Shoebox_Appeal: Christmas gift box campaign
  - Individually wrapped boxes
  - Multiple item categories
  - International distribution
  - Christian literature included
  
Talita_Kum: After-school program, Romania
  - Aramaic: "Get up, little girl"
  - Mark 5:41 biblical reference
  - Educational support focus
  
Daniel_Centre: Residential care, Romania
  - Named after biblical Daniel
  - Ex-care system young men
  - Life skills training focus
  
SERA: Scottish Emergency Relief Agency
  - Partner organization
  - Fire equipment distribution
  - Ukraine aid collaboration
  
CAB: Citizens Advice Bureau
  - Independent advice organization
  - Foodbank referral partner
  - Financial capability support
  
IDP: Internally Displaced Person
  - Displaced within own country
  - Ukraine crisis specific term
  - Humanitarian aid category
  
Roma: Ethnic minority group
  - Significant in Eastern Europe
  - Often marginalized
  - Target population (~50% Talita Kum)
  
Gift_Catalogue: Donor giving option
  - Item-specific donations
  - E.g., "sponsor a meal"
  - Restricted fund mechanism
  
FRS102: Financial Reporting Standard
  - UK and Ireland accounting standard
  - Required for charity accounts
  - Compliance confirmed by directors
  
Basis_Project: Food distribution, Romania
  - Monthly food packages
  - 30 families supported
  - Cluj area focus
  
TK1,_TK2,_TK3: Talita Kum age divisions
  - TK1: Primary school children
  - TK2: Secondary school (10-15)
  - TK3: High school graduates
  
Bonus_Pastor: Hungarian addiction recovery
  - "Good Shepherd" meaning
  - 30+ years operation
  - Long-term therapy focus
  
SERA: Scottish Emergency Relief Agency (defined above)
  
Cornerstone_Trust: Indian partner organization
  - Mumbai red-light district
  - Women and children focus
  - Foster care and day programmes
  
Sargy: Kenyan education partner
  - Rusinga Island
  - 350 children supported
  - Meals and education
  
Christianity_Explored: Discipleship course
  - Booklets and DVDs
  - Serbian edition Blythswood-sponsored
  - Inter-church cooperation tool
  
Go_Relief: Northern Ireland volunteer group
  - Renovation specialists
  - 2018 Daniel Centre renovation
  - Short-term mission model
  
Suits_on_Bikes: Fundraising cycle group
  - Founded 2003
  - Transylvania route
  - Talita Kum support
  - 10th anniversary 2013
  
Common_Good_Fund: Local government fund
  - Inverness-specific
  - Community benefit grants
  - £25K applied for 2024
  
Brains_for_Blythswood: Fundraising quiz
  - Annual October event
  - Virtual format
  - Three regional heats
  - December finals

================================================================================
SECTION 23: DATA QUALITY AND SOURCE NOTES
================================================================================

Primary_Sources:
  - OSCR Charity Register (SC048001, SC021848)
  - Companies House (SC583493)
  - Blythswood Annual Report 2023 (official PDF)
  - Blythswood.org official website
  - Charity Commission NI (NIC104515)
  
Secondary_Sources:
  - Press articles (Inverness Courier, Press & Journal, Ross-shire Journal)
  - Partner organization websites
  - Fundraising platforms (JustGiving, Enthuse)
  - Social media (Facebook)
  - Church partnership communications
  - Third-party charity databases (Endole)
  
Data_Discrepancies_Noted:
  Shoebox_2023: Sources report 84655 (annual report) vs 89000 (other sources)
  Employee_Numbers: 143 (2023 accounts) vs 120 (approximate, other sources)
  Shop_Numbers: 24-26 range depending on source and closures timing
  
Data_Currency:
  Financial_Data: Through 2023 actual, 2024 projected
  Program_Data: Mix of 2023 annual report and 2024/2025 updates
  Leadership: Current as of November 2025
  Contact_Information: Verified from multiple sources
  
Missing_Information:
  - Detailed staff structure beyond senior management
  - Specific salaries/compensation
  - Detailed budget breakdowns by program
  - Historical financial data before 2020
  - Some program-specific metrics
  - Vendor and supplier details
  - IT systems specifications
  - Full list of shop locations
  - Complete list of international partners by country
  
Estimation_Notes:
  - £50000 annual Talita Kum budget (estimated from €50K mentioned)
  - 100000+ annual beneficiaries (calculated from component programs)
  - £50000-75000 foodbank annual need (inferred from grant request context)
  
Data_Verification:
  Cross_Referenced: Multiple sources for key facts
  Official_Sources_Prioritized: OSCR, annual report preferred
  Date_Sensitive: Some information may be historical
  Geographic_Variations: Scotland vs NI data sometimes separate
  
Confidence_Levels:
  High_Confidence:
    - Legal registration details
    - Financial summary data
    - Leadership names and roles
    - Major program descriptions
    - Contact information
    
  Medium_Confidence:
    - Specific beneficiary numbers
    - Some program outcomes
    - Historical timeline details
    - Partnership details
    
  Lower_Confidence:
    - Future plans beyond stated priorities
    - Unverified third-party claims
    - Some operational details
    - Estimates where data unavailable

================================================================================
SECTION 24: DOCUMENT METADATA
================================================================================

Document_Purpose: Master reference document for LLM API grant application generation
Optimization: Structured for machine parsing and natural language understanding
Intended_Use: Automated grant writing, proposal generation, query response
Human_Readability: Secondary priority (API consumption primary)

Creation_Date: 2025-11-19
Created_By: Claude (Anthropic AI)
Created_For: Philip Ross, AI Consultant
Version: 2.0 (Enhanced from v1.0)

Enhancements_from_v1:
  - Added structured data formats
  - Expanded financial analysis
  - Detailed program metrics and outcomes
  - Grant-specific categorization
  - Partnership and network mapping
  - Impact measurement frameworks
  - Historical timeline expansion
  - Risk and opportunity analysis
  - Contact information by function
  - Legal and compliance framework
  - Glossary and definitions
  - Source documentation
  - API-optimized formatting

Document_Structure:
  Total_Sections: 24
  Organization: Logical categorization for grant relevance
  Format: Plain text with clear hierarchical structure
  Encoding: UTF-8
  
Section_Categories:
  Organizational: Sections 1-2, 20-21
  Financial: Section 3
  People: Section 4
  Programs: Sections 5-8
  Ministry: Section 9
  Operations: Sections 10-11
  Strategic: Sections 12, 17
  Impact: Section 13
  Networks: Section 14
  Infrastructure: Section 15
  Historical: Section 16
  Grant_Ready: Section 18
  Reference: Sections 19, 22-24

Maintenance_Notes:
  Update_Frequency: Annually (after annual report publication)
  Key_Triggers_for_Update:
    - New annual report
    - Leadership changes
    - Major program launches or closures
    - Significant financial changes
    - Regulatory changes
    - Contact information updates
    
API_Usage_Guidelines:
  Extraction: Use section headers for targeted information retrieval
  Context: Include relevant sections for comprehensive grant responses
  Synthesis: Combine multiple sections for holistic proposals
  Customization: Adapt language and emphasis for specific funders
  Citation: Reference to Blythswood Annual Report 2023 and OSCR data
  
Grant_Application_Workflow:
  1. Identify funder priorities
  2. Extract relevant sections (especially 18)
  3. Pull supporting data from program sections (5-9)
  4. Include financial data (3) and impact (13)
  5. Demonstrate capacity (2, 4, 14)
  6. Articulate strategic fit (12, 17)
  7. Provide contacts (19)
  8. Customize language and emphasis
  9. Ensure accuracy and compliance (21)

Quality_Assurance:
  Cross_Referencing: Multiple source verification
  Fact_Checking: OSCR and official documents prioritized
  Currency_Verification: Dates and time-sensitive information noted
  Completeness: Grant-relevant information comprehensive
  Accuracy: Known discrepancies documented
  
Limitations:
  - Some information estimated where precise data unavailable
  - Historical information prior to 2020 less detailed
  - International partner details limited to publicly available information
  - Financial projections subject to actual performance
  - Program metrics vary by source and year
  - Some operational details not in public domain

================================================================================
END OF DOCUMENT
================================================================================

Document_Word_Count: ~16000
Last_Updated: 2025-11-19
Next_Review_Due: 2026-08-01 (post-2024 annual report publication)
Version_Control: v2.0.20251119
Character_Count: ~108000

For additional information or clarification:
Contact: Blythswood Care
Phone: 01349 830 777
Email: info@blythswood.org
Website: www.blythswood.org"""

def load_example_grants():
    """
    Load all example grant files from example_grants/ folder.
    Returns combined text of all grants.
    """
    example_grants = []
    grants_folder = os.path.join(os.path.dirname(__file__), 'example_grants')
    
    # Check if folder exists
    if not os.path.exists(grants_folder):
        print("⚠️  Warning: example_grants/ folder not found")
        return ""
    
    # Load all .txt files from the folder
    try:
        files = sorted([f for f in os.listdir(grants_folder) if f.endswith('.txt')])
        
        if not files:
            print("⚠️  Warning: No .txt files found in example_grants/")
            return ""
        
        for filename in files:
            filepath = os.path.join(grants_folder, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                example_grants.append(content)
                print(f"✓ Loaded: {filename}")
        
        # Combine all grants with separator
        combined = "\n\n=== NEXT GRANT ===\n\n".join(example_grants)
        print(f"✓ Total example grants loaded: {len(files)}")
        return combined
        
    except Exception as e:
        print(f"⚠️  Error loading example grants: {e}")
        return ""

# ===================================================================
# HELPER FUNCTIONS
# ===================================================================

def get_master_doc():
    """Returns the master document."""
    return MASTER_DOC

def get_past_grants():
    """Returns combined example grants from example_grants/ folder."""
    return load_example_grants()

def get_organization_name():
    """Returns the organization name."""
    return "Blythswood Care"
