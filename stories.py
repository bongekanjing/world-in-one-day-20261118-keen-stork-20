"""The 18 November 2026 front page: story list, figures and provenance.

Every item below happened, or was first reported, on Wednesday 18 November 2026.
"""

DATA = {
    "paper": "The World in One Day",
    "date_lines": ["Wednesday", "18 November 2026"],
    "standfirst": "Iran strikes a US base in Kuwait  ·  Trump lands in Shenzhen  ·  "
                  "Drone raids cut Russia's refining by half",
    "region_order": ["EUROPE", "THE AMERICAS", "ASIA-PACIFIC", "MIDDLE EAST",
                     "AFRICA", "OCEANIA", "WORLD"],
    "figures": [
        ("146,000", "protesters across France in a cost-of-living march"),
        ("45%", "of Russia's refining offline after drone raids"),
        ("$115.8bn", "Nvidia's quarterly revenue, reported on Tuesday"),
        ("50,000", "displaced by clashes in southern Ethiopia"),
        ("11,000", "arrivals in the Canaries this month"),
        ("2,500", "Salvadoran troops deploying to Haiti"),
    ],
    "brief_header": "Also on Wednesday 18 November",

    "stories": [
        # ---------------- leads (illustrated) ----------------
        dict(n=1, region="MIDDLE EAST", where="Kuwait City", art="missile",
             caption="Drones over Ali Al Salem: Iran's retaliation for the Qeshm raid",
             head="Iran strikes a US air base in Kuwait as Trump flies to Shenzhen",
             text="Army drones targeted Patriot batteries before dawn, Kuwait said, "
                  "calling it a direct threat. Bahrain downed a third attack in a week "
                  "and a Houthi missile aimed at Riyadh was intercepted.",
             lon=47.98, lat=29.38),
        dict(n=2, region="ASIA-PACIFIC", where="Shenzhen", art="flags",
             caption="On the tarmac: Xi meets Trump before Thursday's trilateral",
             head="Xi greets Trump in Shenzhen ahead of a three-power summit",
             text="Xi met Air Force One on the tarmac, a gesture Beijing rarely makes, "
                  "before Thursday's trilateral with Vladimir Putin, the first between "
                  "the leaders of the three nuclear powers.",
             lon=114.06, lat=22.54),
        dict(n=3, region="EUROPE", where="Kyiv", art="chart",
             caption="Refineries hit: 45% of November's processing is offline",
             head="Drone raids cut Russia's oil refining by nearly half",
             text="Long-range strikes have taken 45% of November's refining capacity "
                  "offline, Ukrainian officials said. Polish reporters say Moscow "
                  "planned a mass-casualty attack near Kaliningrad.",
             lon=30.52, lat=50.45),

        # ---------------- second tier (illustrated) ----------------
        dict(n=4, region="THE AMERICAS", where="Caracas", mid=True, art2="crowd",
             head="Hegseth flies to Caracas and signs a military pact",
             text="The defence secretary agreed closer cooperation, the clearest "
                  "American opening to Caracas in years.",
             lon=-66.9, lat=10.49),
        dict(n=5, region="EUROPE", where="Antalya", mid=True, art2="storm",
             head="COP31 deadlocks over who pays for the damage",
             text="Ministers launched a global check as the fossil-fuel text stalled. "
                  "Panama's minister called the talks hostage to an oil mafia.",
             lon=30.71, lat=36.9),
        dict(n=6, region="THE AMERICAS", where="Washington", mid=True, art2="court",
             head="Peltola flips Alaska's Senate seat to the Democrats",
             text="The Yup'ik former congresswoman unseated two-term Republican Dan "
                  "Sullivan, the AP projected, widening the Democratic majority.",
             lon=-77.04, lat=38.9),
        dict(n=7, region="ASIA-PACIFIC", where="Seoul", mid=True, art2="missile",
             head="IAEA finds Yongbyon's enrichment hall has grown",
             text="Rafael Grossi reported a new extension at the plant; Marco Rubio "
                  "said Trump is serious about meeting Kim Jong Un.",
             lon=126.98, lat=37.57),
        dict(n=8, region="THE AMERICAS", where="Brasilia", mid=True, art2="money",
             head="Senate approves Lula's fiscal package",
             text="The government called the vote essential to hit its targets; "
                  "investors saw a first step only.",
             lon=-47.93, lat=-15.79),
        dict(n=9, region="MIDDLE EAST", where="Gaza", mid=True, art2="crowd",
             head="Trump's Board of Peace faults Israel and Hamas alike",
             text="A 12-page report warned the ceasefire may collapse as tanks pushed "
                  "into central Gaza and three Palestinians were killed.",
             lon=34.47, lat=31.5),
        dict(n=10, region="THE AMERICAS", where="Port-au-Prince", mid=True, art2="crowd",
             head="Thousands march for the Salvadoran deployment",
             text="Port-au-Prince cheered Bukele's soldiers as Haiti formalised the "
                  "security pact and 2,500 troops prepared to deploy.",
             lon=-72.34, lat=18.54),
        dict(n=11, region="EUROPE", where="Paris", mid=True, art2="crowd",
             head="Unions vow more strikes after a day of action",
             text="French unions said they would keep up pressure on the government "
                  "over pay after Tuesday's nationwide walkout drew 146,000.",
             lon=2.35, lat=48.86),
        dict(n=12, region="AFRICA", where="Addis Ababa", mid=True, art2="storm",
             head="Moyale clashes displace more than 50,000",
             text="Fighting over a regional flag spread across seven southern "
                  "districts, aid agencies said.",
             lon=38.75, lat=9.03),
        dict(n=13, region="EUROPE", where="London", mid=True, art2="money",
             head="Bailey says rates are not on a pre-set path",
             text="The Bank of England governor pointed to the length of the Iran "
                  "war as the reason for caution.",
             lon=-0.13, lat=51.51),

        # ---------------- briefs ----------------
        dict(n=14, region="OCEANIA", where="Canberra",
             head="Australia sanctions settlers, a day after Britain",
             lon=149.13, lat=-35.28),
        dict(n=15, region="MIDDLE EAST", where="Sanaa",
             head="Coalition strikes 60 Houthi targets in a day",
             lon=44.21, lat=15.35),
        dict(n=16, region="AFRICA", where="Rabat",
             head="Rabat plans to build 40% of its arms at home",
             lon=-6.84, lat=33.97),
        dict(n=17, region="ASIA-PACIFIC", where="Beijing",
             head="Nvidia halts AI chip shipments to China",
             lon=116.4, lat=39.9),
        dict(n=18, region="THE AMERICAS", where="Mexico City",
             head="Sheinbaum calls US trade talks very far along",
             lon=-99.13, lat=19.43),
        dict(n=19, region="THE AMERICAS", where="Washington",
             head="Pulisic's bicycle kick ends Pochettino's US reign",
             lon=-77.04, lat=38.9),
        dict(n=20, region="EUROPE", where="Geneva",
             head="Gut egoviruses found in millions of people",
             lon=6.14, lat=46.2),
        dict(n=21, region="THE AMERICAS", where="Buenos Aires",
             head="Milei tells Congress to pass his budget",
             lon=-58.38, lat=-34.6),
        dict(n=22, region="AFRICA", where="Pretoria",
             head="Five appear in court under the mercenary law",
             lon=28.19, lat=-25.75),
        dict(n=23, region="THE AMERICAS", where="Boca Chica",
             head="SpaceX studies the data from Starship's first tower catch",
             lon=-97.15, lat=25.99),
        dict(n=24, region="AFRICA", where="Kinshasa",
             head="Ebola outbreak passes 5,500 deaths",
             lon=15.31, lat=-4.32),
        dict(n=25, region="OCEANIA", where="Port Vila",
             head="Vanuatu asks COP31 to reform the summit process",
             lon=168.32, lat=-17.73),
        dict(n=26, region="ASIA-PACIFIC", where="Manila",
             head="ASEAN and its partners press the Manila agenda",
             lon=120.98, lat=14.6),
        dict(n=27, region="EUROPE", where="Berlin",
             head="Germany clears a further weapons package for Kyiv",
             lon=13.4, lat=52.52),
        dict(n=28, region="MIDDLE EAST", where="Dubai",
             head="A tanker is hit off Oman and insurance rates jump",
             lon=55.27, lat=25.2),
        dict(n=29, region="ASIA-PACIFIC", where="New Delhi",
             head="India and Canada near a defence pact for December",
             lon=77.21, lat=28.61),
        dict(n=30, region="AFRICA", where="Nairobi",
             head="Kenya counts 71 flood deaths as the rains go on",
             lon=36.82, lat=-1.29),
        dict(n=31, region="WORLD", where="Geneva",
             head="WHO warns antibiotics are failing against common infections",
             lon=6.15, lat=46.21),
        dict(n=32, region="WORLD", where="The Hague",
             head="The ICJ sets its Rohingya judgment for Thursday morning",
             lon=4.3, lat=52.07),
        dict(n=33, region="OCEANIA", where="Sydney",
             head="Economists warn Australia shows the hallmarks of a recession",
             lon=151.21, lat=-33.87),
        dict(n=34, region="EUROPE", where="Rome",
             head="Italy's parliament opens the citizenship referendum debate",
             lon=12.5, lat=41.9),
        dict(n=35, region="ASIA-PACIFIC", where="Tokyo",
             head="Takaichi and Xi shake hands at APEC as ties stay frosty",
             lon=139.69, lat=35.69),
        dict(n=36, region="EUROPE", where="Brussels",
             head="The EU's proposed 45bn loan for Ukraine awaits a decision",
             lon=4.35, lat=50.85),
        dict(n=37, region="AFRICA", where="Mogadishu",
             head="Somalia's constitutional overhaul tests its federal bargain",
             lon=45.34, lat=2.05),
        dict(n=38, region="ASIA-PACIFIC", where="Jakarta",
             head="Governments warn a Java logging flaw leaves systems exposed",
             lon=106.85, lat=-6.21),
        dict(n=39, region="MIDDLE EAST", where="Baghdad",
             head="Six French ISIL members sentenced to life by an Iraqi court",
             lon=44.36, lat=33.31),
        dict(n=40, region="EUROPE", where="Amsterdam",
             head="Europe's scrap exporters fight over waste shipments",
             lon=4.9, lat=52.37),
        dict(n=41, region="AFRICA", where="Brazzaville",
             head="Sassou-Nguesso opens a mediation between Tshisekedi and Ruto",
             lon=15.28, lat=-4.27),
        dict(n=42, region="ASIA-PACIFIC", where="Dhaka",
             head="Four killed as a shutdown grips Bangladesh",
             lon=90.41, lat=23.81),
        dict(n=43, region="THE AMERICAS", where="Ottawa",
             head="Carney says Canada will not back down in trade talks",
             lon=-75.7, lat=45.42),
        dict(n=44, region="WORLD", where="Bangkok",
             head="Asia's reproductive-genetics meeting ends with a call to share methods",
             lon=100.5, lat=13.75),
    ],

    "date_check": (
        "every item on this page was reported or happened on Wednesday 18 November "
        "2026. Thursday's trilateral between Trump, Xi and Putin in Shenzhen is "
        "named as a scheduled event, not as news of this day. Figures are the counts "
        "given by the reporting agency named in each item."
    ),

    "footer": (
        "The World in One Day  ·  No. 322  ·  free  ·  Compiled 18 November 2026. "
        "Disputed claims are attributed to whoever made them. Counts on this page are "
        "computed from the stories themselves. Sources: AP, Reuters, AFP, Xinhua, "
        "Kyodo, The Hindu, BBC, IAEA, UN OCHA."
    ),
}
