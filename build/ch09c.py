# Chapter 9, pages 9.8 to 9.11. Coordinates are [longitude, latitude].
from common import c, q

S = {
 # 9.8
 'brit-menander': ("Encyclopaedia Britannica, \"Menander\" (Indo-Greek king)", "https://www.britannica.com/biography/Menander-Indo-Greek-king"),
 'shiraz-rabatak': ("\"The Rabatak inscription\", Shiraz University journal", "https://tesl.shirazu.ac.ir/article_255.html"),
 'carc-chronology': ("Classical Art Research Centre, Oxford, \"Problems of chronology in Gandharan art\": abstracts (Falk, Cribb, Behrendt)", "https://www.carc.ox.ac.uk/PublicFiles/media/Problems%20of%20Chronology%20abstracts.pdf"),
 'met-gandhara': ("The Met, The Art of Gandhara in the Metropolitan Museum of Art", "https://www.metmuseum.org/art/metpublications/The_Art_of_Gandhara_in_The_Metropolitan_Museum_of_Art"),
 'smarthistory-buddha': ("Smarthistory, on the first images of the Buddha", "https://smarthistory.org/?p=48116"),
 'equinox-bajaur': ("Paul Harrison (ed.), Setting Out on the Great Way, ch. 9, on the Bajaur Mahayana sutra (Equinox)", "https://equinoxreligionlibrary.com/projects/abstracts-hub/resource-collection/mahayana-buddhism/resource/harrison-setting-out-on-the-great-way-9"),
 'brit-satavahana': ("Encyclopaedia Britannica, \"Satavahana dynasty\"", "https://britannica.com/topic/Satavahana-dynasty"),
 'brit-sangam': ("Encyclopaedia Britannica, \"Sangam literature\"", "https://www.britannica.com/art/shangam-literature"),
 'efeo-arikamedu': ("École française d'Extrême-Orient, Begley et al., The Ancient Port of Arikamedu, vol. 2", "https://publications.efeo.fr/en/livres/380_the-ancient-port-of-arikamedu"),
 'muziris-pattanam': ("Muziris Heritage Project, \"Pattanam\"", "https://muzirisheritage.org/pattanam.php"),
 'tnm-keeladi2026': ("The News Minute, 'Keeladi archaeologist rejects ASI review, seeks immediate release of excavation report' (5 February 2026)", "https://www.thenewsminute.com/tamil-nadu/keeladi-archaeologist-rejects-asi-review-seeks-immediate-release-of-excavation-report"),
 'week-keeladi': ("The Week, \"Explained: is ASI expert Amarnath Ramakrishna being targeted over Keeladi excavations?\" (26 May 2025)", "https://www.theweek.in/news/india/2025/05/26/explained-is-asi-expert-amarnath-ramakrishna-being-targeted-over-keeladi-excavations.html"),
 # 9.9
 'epgp-allahabad': ("P. Bhaskar Reddy, \"Allahabad pillar inscription of Samudragupta\", e-PG Pathshala (UGC/INFLIBNET)", "https://epgp.inflibnet.ac.in/epgpdata/uploads/epgp_content/S000829IC/P001689/M022047/ET/1504072712P08-M33-AllahabadPillarInscriptionofSamudragupta-ET.pdf"),
 'coinindia-samudra': ("CoinIndia, Samudragupta gallery", "https://www.coinindia.com/galleries-samudragupta.html"),
 'brit-cg2': ("Encyclopaedia Britannica, \"Chandragupta II\"", "https://www.britannica.com/biography/Chandragupta-II"),
 'map-udayagiri': ("MAP Academy, \"Udayagiri\"", "https://mapacademy.io/?p=3107"),
 'brit-kalidasa': ("Encyclopaedia Britannica, \"Kalidasa\"", "https://www.britannica.com/biography/Kalidasa"),
 'brit-aryabhata': ("Encyclopaedia Britannica, \"Aryabhata I\"", "https://www.britannica.com/biography/Aryabhata-I"),
 'ox-bakhshali': ("University of Oxford (GLAM), Bodleian announcement on the Bakhshali manuscript (14 September 2017)", "https://www.glam.ox.ac.uk/node/218481"),
 'indology-bakhshali': ("INDOLOGY list, 15 September 2017: folio-by-folio radiocarbon ranges from the Bodleian curator", "https://list.indology.info/pipermail/indology/2017-September/046594.html"),
 'hssa-bakhshali': ("Plofker, Keller, Hayashi, Montelle and Wujastyk, \"The Bakhshālī manuscript: a response to the Bodleian Library's radiocarbon dating\", History of Science in South Asia 5 (2017)", "https://journals.library.ualberta.ca/hssa/index.php/hssa/article/view/22"),
 'sh-deogarh': ("Smarthistory / MAP Academy, \"Dashavatara temple, Deogarh\"", "https://smarthistory.org/dashavatara-temple-deogarh"),
 'dna-golden': ("M. A. Kalra, \"Gupta dynasty: the golden age versus the age of feudalism\", DNA India (2017)", "https://dnaindia.com/lifestyle/report-gupta-dynasty-the-golden-age-versus-the-age-of-feudalism-2444781"),
 'kervan-manu': ("Review of Squarcini and Cuneo's translation of the Manusmriti, Kervan 28.2 (2024)", "https://ojs.unito.it/index.php/kervan/article/download/11494/9517/37984"),
 'brit-gupta': ("Encyclopaedia Britannica, \"Gupta dynasty\"", "https://www.britannica.com/topic/Gupta-dynasty"),
 'rezakhani-huns': ("Khodadad Rezakhani, \"Iranian Huns\", Iranologie", "https://iranologie.com/the-history-page/the-sasanian-empire-2/iranian-huns/"),
 # 9.10
 'so-mahinda': ("Sunday Observer (Sri Lanka), on William Dalrymple and Buddhism before Mahinda (5 January 2025)", "https://www.sundayobserver.lk/2025/01/05/news-features/41654/buddhism-was-in-existence-in-sri-lanka-before-the-advent-of-arahant-mahinda-historian-william-dalrymple"),
 'brit-mahavamsa': ("Encyclopaedia Britannica, \"Mahavamsa\"", "https://www.britannica.com/topic/Mahavamsa"),
 'palumbo2007': ("Antonello Palumbo, \"Literary evidence on Han Buddhism\" (SOAS, 2007)", "https://core.ac.uk/download/19090669.pdf"),
 'scroll-whitehorse': ("Scroll.in, \"Buddhism's spread from India to China started with a Han emperor's dream\" (2024)", "https://scroll.in/magazine/1075459/buddhisms-spread-from-india-to-china-started-with-a-han-emperors-dream"),
 'iias-anshigao': ("International Institute for Asian Studies, Leiden, on the An Shigao dictionary project", "https://iias.asia/event/understanding-earliest-chinese-buddhist-translations-progress-report-shigao-dictionary"),
 'brit-kumarajiva': ("Encyclopaedia Britannica, \"Kumarajiva\"", "https://www.Britannica.com/biography/Kumarajiva"),
 'brit-faxian': ("Encyclopaedia Britannica, \"Faxian\"", "https://www.britannica.com/biography/Faxian"),
 'yale-kongwangshan': ("Yale MacMillan Center, \"The date of Kongwangshan reconsidered\" (Minku Kim, November 2022)", "https://macmillan.yale.edu/events/2022-11/date-kongwangshan-reconsidered"),
 'unesco-mogao': ("UNESCO World Heritage Centre, \"Mogao Caves\"", "https://whc.unesco.org/en/list/440"),
 'unesco-yungang': ("UNESCO World Heritage Centre, \"Yungang Grottoes\"", "https://whc.unesco.org/en/list/1039"),
 # 9.11
 'scheidel-romechina': ("Walter Scheidel, \"From the 'Great Convergence' to the 'First Great Divergence'\", Stanford Rome and China project", "https://web.stanford.edu/~scheidel/Rome%26China.pdf"),
 'alfani2025': ("Alfani, Bolla and Scheidel, inequality in ancient empires (Han, Rome, Aztec), Nature Communications 16 (2025)", "https://iris.unibocconi.it/retrieve/afc74823-36a4-4b06-8c54-a5c3b19ed701/AlfaniBollaScheidel_InequalityAncientEmpires.pdf"),
 'giele-heidelberg': ("Enno Giele, Han and Rome compared, Marsilius-Kolleg, Heidelberg University", "https://www.marsilius-kolleg.uni-heidelberg.de/md/einrichtungen/mk/publikationen/10_mk_jahresbericht_giele.pdf"),
 'bielenstein-bureaucracy': ("Hans Bielenstein, The Bureaucracy of Han Times (Cambridge), conclusion", "https://core-prod.cambridgecore.org/core/books/bureaucracy-of-han-times/conclusion/A4E49FAD526A8335DF29EAB9F1A5BC3F"),
 'scheidel-friesen2': ("Scheidel and Friesen, \"The size of the economy and the distribution of income in the Roman empire\", Journal of Roman Studies 99 (2009)", "https://cambridge.org/core/services/aop-cambridge-core/content/view/ADBB8C20D8DFDB7F5A8B209718AF7942/S0075435800000071a.pdf/size_of_the_economy_and_the_distribution_of_income_in_the_roman_empire.pdf"),
 'bmcr-statepower': ("Review of Scheidel (ed.), State Power in Ancient China and Rome (2015), Bryn Mawr Classical Review 2015.09.24", "https://bmcr.brynmawr.edu/?p=36641"),
 'loewe2025': ("Michael Loewe, Imperial Institutions in Ancient Rome and Early China (Bloomsbury, 2025)", "https://backstory.london/products/9781350445123"),
 'camws-army': ("CAMWS 2014 abstract on the size of the Roman imperial army", "https://camws.org/meeting/2014/abstracts/individual/038.RomanImperialArmy.pdf"),
 'scheidel-escape': ("Walter Scheidel, Escape from Rome (Princeton, 2019), introduction", "https://web.stanford.edu/~scheidel/Escape%20from%20Rome.pdf"),
}

C = {
 # 9.8
 'c-menander': c("The Indo-Greek king Menander (about 160-135 BCE) ruled from the Kabul valley into the Punjab and may have raided as far as Pataliputra.", 'approx', ['brit-menander'], "Britannica gives his dates with question marks; much Indo-Greek history is rebuilt from coins."),
 'c-milinda': c("A Pali Buddhist text, the Questions of Milinda, shows Menander in debate with the monk Nagasena, and Buddhist tradition says he converted.", 'tradition', ['brit-menander'], "The text shows a tradition; whether Menander became a Buddhist is not proven. A wheel on some of his coins is probably Buddhist."),
 'c-rabatak': c("An inscription found at Rabatak in Afghanistan in 1993, in the Bactrian language written in Greek letters, lists the Kushan kings before Kanishka: Kujula Kadphises, Vima Taktu and Vima Kadphises.", 'consensus', ['shiraz-rabatak'], show=False),
 'c-kanishka-date': c("Year 1 of Kanishka's era is now usually placed in 127 CE.", 'debated', ['carc-chronology'], "Harry Falk's date, which Joe Cribb calls 'widely accepted'; older scholarship put Kanishka decades earlier, often at 78 CE. Because inscriptions and statues are dated in his era, the choice moves the whole chronology of Gandharan art."),
 'c-gandhara': c("In Gandhara, in today's north-west Pakistan and eastern Afghanistan, Buddhist narrative reliefs appear from the early 1st century CE; the region's Buddhist art flourished for some four centuries.", 'approx', ['met-gandhara', 'carc-chronology'], "Kurt Behrendt argues much 'Kushan' Gandharan art actually dates from the 3rd to 6th centuries."),
 'c-buddha-image': c("Early Indian art showed the Buddha only through symbols such as footprints and empty thrones; images of him in human form appear around the turn of the era in two Kushan-ruled centres, Gandhara and Mathura.", 'debated', ['smarthistory-buddha'], "That the images began under Kushan rule is agreed; Alfred Foucher argued Gandhara came first, Ananda Coomaraswamy Mathura."),
 'c-bajaur': c("A Mahayana sutra from Bajaur, written in Gandhari in the 1st or 2nd century CE, is among the oldest surviving witnesses to Mahayana Buddhism.", 'approx', ['equinox-bajaur'], "Dated by its handwriting; the edition is still in progress."),
 'c-satavahana': c("The Satavahanas built the first empire of the Deccan; wealth from trade with the Roman world paid for generous patronage of both Buddhist and Brahmin communities.", 'debated', ['brit-satavahana'], "Their start is dated anywhere from the 3rd to the late 1st century BCE; their greatest king, Gautamiputra Satakarni, ruled about 106-130 CE."),
 'c-sangam': c("The Tamil poems of the Sangam anthologies, dated to about the 1st-4th centuries CE, are divided into akam (love) and puram (war and kingship); tradition links them to poets' academies at Madurai.", 'approx', ['brit-sangam'], "The dates are approximate and the academies are traditional."),
 'c-arikamedu': c("Arikamedu, near Puducherry, is the most important excavated site of the sea trade between India and the Roman Mediterranean; excavations in 1989-92 found Roman amphorae and Chinese ceramics.", 'consensus', ['efeo-arikamedu'], show=False),
 'c-pattanam': c("At Pattanam in Kerala, excavators have found Roman amphorae and tableware, early Chera coins and a wharf, from a settlement occupied from about the 2nd century BCE.", 'debated', ['muziris-pattanam'], "The excavators argue Pattanam is ancient Muziris (see 8.11); the identification is not yet certain."),
 'c-keeladi': c("At Keeladi in Tamil Nadu, the excavator's report dates the first phase of an urban settlement to the 8th-5th centuries BCE; in 2025 the Archaeological Survey of India asked him to rewrite it, he declined, and in early 2026 he rejected an ASI committee's critique and demanded that the report be published.", 'debated', ['week-keeladi', 'tnm-keeladi2026'], "New and politically charged: the dispute is partly about evidence and partly about how old Tamil urban culture is."),
 # 9.9
 'c-gupta-era': c("The Gupta era began in 319/320 CE, and the dynasty held northern India from the early 4th to the 6th century.", 'approx', ['epgp-allahabad', 'brit-gupta'], "The end date depends on how one counts the later, weaker kings."),
 'c-allahabad': c("Samudragupta (about 335-375) had his court poet Harishena carve a eulogy on an old Ashokan pillar, listing kings of the north 'uprooted', twelve southern kings 'captured and released', and foreign rulers paying homage.", 'debated', ['epgp-allahabad'], "The text is certain; its claims, as one specialist puts it, 'can hardly be taken in their face value'."),
 'c-samudra-coins': c("Samudragupta's gold coins show him as an archer, as the performer of the royal horse sacrifice, and playing a stringed vina.", 'consensus', ['coinindia-samudra'], show=False),
 'c-cg2': c("Chandragupta II (about 380-415) conquered the Shaka kingdoms of western India between about 388 and 409.", 'approx', ['brit-cg2'], "Dates are reconstructed from coins and inscriptions."),
 'c-udayagiri': c("At Udayagiri near Vidisha, an inscription of 401 CE names Chandragupta II at the dedication of a cave temple, beside a colossal relief of Vishnu as the boar Varaha.", 'consensus', ['map-udayagiri'], show=False),
 'c-kalidasa': c("Kalidasa, the greatest Sanskrit poet and dramatist, is often placed at the court of Chandragupta II.", 'debated', ['brit-kalidasa'], "His date is only known to fall before 634 CE; the Gupta link is, in Britannica's words, 'the most convincing but most conjectural' view."),
 'c-aryabhata': c("Aryabhata, born in 476, wrote his Aryabhatiya in about 499; he used decimal place value, gave pi as about 3.1416, and argued that the Earth rotates.", 'consensus', ['brit-aryabhata'], show=False),
 'c-bakhshali': c("In 2017 the Bodleian Library announced that the Bakhshali manuscript, which uses a dot for zero, dates 'as early as the 3rd or 4th century'.", 'debated', ['ox-bakhshali', 'indology-bakhshali', 'hssa-bakhshali'], "Its three tested leaves gave very different dates (224-383, 680-779 or 790-868, and 885-993 CE). Kim Plofker, Dominik Wujastyk and colleagues argue that the latest leaf dates the copying, and criticised the Bodleian for announcing the results by press release without peer review."),
 'c-brahmagupta': c("The first text to treat zero as a number in its own right, with rules for calculating with it, is Brahmagupta's of 628 CE.", 'consensus', ['ox-bakhshali'], show=False),
 'c-deogarh': c("The Dashavatara temple at Deogarh, of the early 6th century, is the earliest north Indian temple built entirely of stone with a tower over its shrine.", 'approx', ['sh-deogarh'], "Its date is set by style."),
 'c-golden-age': c("Calling the Gupta period India's 'golden age' is disputed.", 'debated', ['dna-golden'], "The label goes back to nationalist historians before independence; Marxist historians answer that its achievements served an upper-caste elite while caste hierarchy hardened."),
 'c-manu': c("The Manusmriti, the most influential text on dharma and caste, was composed in about the 2nd century CE according to Patrick Olivelle, the view most scholars follow.", 'debated', ['kervan-manu'], "Others, such as Federico Squarcini and Daniele Cuneo, prefer the 2nd century BCE."),
 'c-huns': c("From about 440 the Alchon Huns held Gandhara; under Toramana and Mihirakula (about 490-528) they repeatedly defeated Gupta armies, and the empire declined.", 'approx', ['rezakhani-huns', 'brit-gupta'], "Dates are approximate."),
 # 9.10
 'c-mahinda': c("Sri Lankan tradition says Ashoka's son Mahinda converted the king at Anuradhapura in about 250 BCE, and his sister brought a cutting of the Bodhi tree.", 'tradition', ['so-mahinda', 'brit-mahavamsa'], "The story comes from the Mahavamsa, a chronicle written some seven centuries later; William Dalrymple argues Buddhism reached the island earlier."),
 'c-liuying': c("The earliest firm evidence for Buddhism in China is an imperial edict of 65 CE praising Liu Ying, Prince of Chu, for honouring the Buddha and feeding monks and lay followers.", 'consensus', ['palumbo2007'], show=False),
 'c-mingdi': c("The story that Emperor Ming dreamed of a golden man, sent envoys to India and founded the White Horse Temple at Luoyang is a pious legend.", 'tradition', ['palumbo2007', 'scroll-whitehorse'], "Antonello Palumbo notes that Henri Maspero showed in 1910 that the story 'bears all the traits of a pious legend', and argues that the mission to India was probably absent from Yuan Hong's original Hou Han ji (4th century) and was added by later editors."),
 'c-anshigao': c("An Shigao, a Parthian monk working in Luoyang from about 148 to 170, is 'the first undoubtedly historical personality in Chinese Buddhism'.", 'consensus', ['iias-anshigao'], show=False),
 'c-kumarajiva': c("Kumarajiva (344-413), brought to China as a captive and settled at Chang'an in 401, became one of the greatest translators of Buddhist texts into Chinese.", 'consensus', ['brit-kumarajiva'], show=False),
 'c-faxian': c("The monk Faxian left China in 399, crossed Central Asia to India, studied there and in Sri Lanka, and sailed home by way of South-East Asia, landing in Shandong; his Record of Buddhist Kingdoms describes the journey.", 'approx', ['brit-faxian'], "His return is dated 412-414; he brought back and translated monastic rules and sutras. The island where he waited on the way home was probably Java."),
 'c-kongwangshan': c("Buddhist-looking reliefs on the cliffs of Kongwangshan, near Lianyungang, are usually dated to the Eastern Han.", 'debated', ['yale-kongwangshan'], "Minku Kim (2022) argues they date from the 6th century at the earliest, partly because of the later Kanishka date."),
 'c-mogao': c("The Mogao caves at Dunhuang were begun in 366 CE; 492 decorated caves survive.", 'consensus', ['unesco-mogao'], show=False),
 'c-yungang': c("The Yungang grottoes near Datong were carved under the Northern Wei from the mid-5th to the early 6th century and hold about 51,000 statues.", 'consensus', ['unesco-yungang'], show=False),
 # 9.11
 'c-size-similar': c("At their height the Han and Roman empires each covered about 4 million km² and held some 60 million people or more.", 'approx', ['scheidel-romechina', 'alfani2025'], "Han figures come from the census of 2 CE (57.7 to 59.6 million registered); Roman estimates run from 'c. 60+ million' (Scheidel) to 70-75 million (Scheidel and Friesen 2009; Alfani, Bolla and Scheidel 2025)."),
 'c-inequality2025': c("A 2025 study estimates that income inequality was similar in both empires, with a Gini coefficient of about 0.48 for the Han in 2 CE and 0.46 for Rome in about 165 CE; the top 1 percent took about 26 percent of income in Han China and 19 percent in Rome.", 'approx', ['alfani2025'], "New and model-based: the figures are reconstructed from urbanisation and population density, not from tax records."),
 'c-han-officials': c("The Han history gives the number of officials, from the chancellor down to clerks, as 130,285 in 5 BCE (Hans Bielenstein's reading); Liang Cai cites 120,285 for 2 CE.", 'approx', ['bielenstein-bureaucracy', 'cai2019'], "The two numbers reflect different readings of the same passage; either way, some 120,000-130,000 officials. The bureaucracy of a single commandery, Donghai, is known from an excavated register."),
 'c-rome-elite': c("Rome governed with a far smaller elite: about 600 senators and perhaps 20,000 equestrians, and state spending of roughly 5 percent of output.", 'approx', ['scheidel-friesen2'], "Estimates by Walter Scheidel and Steven Friesen (2009)."),
 'c-low-tax': c("Both empires were, in Walter Scheidel's phrase, 'low-tax regimes'; Rome paid its top officials far more and spent more on its army, while the Han spent a much larger share of its defence budget on subsidies to foreign peoples.", 'debated', ['bmcr-statepower'], "A reviewer warns that such comparisons involve heavy conjecture."),
 'c-loewe': c("Michael Loewe argues that Rome was governed largely by military officials, the Han by roughly 130,000 trained professional administrators.", 'debated', ['loewe2025'], "An interpretation (2025); Roman provincial government also relied on many civilian officials and local elites."),
 'c-coins-compare': c("The Han wuzhu was a single low-value coin cast in bronze, while Rome struck coins in gold, silver and bronze; one source reports some 28 billion wuzhu made in the coin's first 110 years.", 'approx', ['giele-heidelberg'], "The contrast is agreed; the 28 billion is a figure from the Han histories."),
 'c-roman-army': c("The Roman army's size is uncertain: Augustus kept 28 legions, reduced to 25 after the Varus disaster, and estimates of total strength with auxiliaries run from 200,000 to a million.", 'debated', ['camws-army'], "Most modern estimates for the early empire cluster in the lower part of that range."),
 'c-divergence': c("After a brief reunion under the Jin (280-c. 316), China was reunified in 589 and repeatedly afterwards, while no empire ever again ruled the whole Roman world; Walter Scheidel calls this the 'First Great Divergence'.", 'debated', ['scheidel-romechina', 'scheidel-escape'], "Scheidel credits exposure to the steppe, geography and the nature of post-imperial regimes, and argues Europe's lasting fragmentation was 'an indispensable precondition' for its later growth; others stress different causes."),
}

# ---------------------------------------------------------------- 9.8
P8 = {
 'title': "After the Mauryas", 'sub': "Greeks, Kushans and the Tamil south, c. 185 BCE-300 CE",
 'lede': "For five centuries after Ashoka no single power ruled India. Greek kings from Bactria, nomad Kushans from Central Asia and merchant kingdoms in the Deccan and the far south made the subcontinent a crossroads, and in this crowded world the first images of the Buddha were carved.",
 'body': [
  "The Greeks of Bactria (see 8.4) crossed the Hindu Kush as the Mauryas fell. Their best-known king, Menander, ruled the Punjab, [[c-menander]] and a Buddhist text remembers him debating a monk. [[c-milinda]] Then came the Kushans, a nomad people from Central Asia, whose empire at its height ran from the Oxus to the Ganges. An inscription found in 1993 gave their royal line, [[c-rabatak]] but the date of their greatest king, Kanishka, has been argued about for a century. [[c-kanishka-date]]",
  "Under the Kushans the Buddha was first shown in human form, in Gandhara in a style borrowed from Greek and Roman sculpture and at Mathura in an Indian one. [[c-buddha-image]] [[c-gandhara]] New Buddhist scriptures, the Mahayana sutras, were already being copied in Gandhara. [[c-bajaur]]",
  "Further south, the Satavahanas built an empire in the Deccan on the profits of trade with Rome. [[c-satavahana]] On the coasts, ports such as Arikamedu and Pattanam received Roman wine and oil jars, [[c-arikamedu]] [[c-pattanam]] and the Tamil kingdoms produced the Sangam poems, among the finest early literature of India. [[c-sangam]] How old Tamil urban culture is has become a political question. [[c-keeladi]]",
  {'table': {'head': ["Power", "Where", "When", "Remembered for"], 'rows': [
    ["Indo-Greeks", "Bactria, Punjab", "c. 200 BCE-1st century CE", "Menander; bilingual coins"],
    ["Kushans", "Bactria to the Ganges", "1st-3rd centuries CE", "Kanishka; Gandhara and Mathura art"],
    ["Satavahanas", "Deccan", "1st century BCE-3rd century CE", "trade wealth; Buddhist cave monasteries"],
    ["Tamil kingdoms", "far south", "named by Ashoka (3rd century BCE); Sangam poems c. 1st-4th centuries CE", "Sangam poetry; Roman trade"]], 'note': "[[c-menander]] [[c-kanishka-date]] [[c-satavahana]] [[c-sangam]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 76.0, 'lat': 22.5, 'zoom': 9}, 'caption': "India after the Mauryas, c. 185 BCE-300 CE", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [68.0, 37.6], 'label': 'BACTRIA', 'size': 10}, {'ll': [74.0, 32.0], 'label': 'PUNJAB', 'size': 9}, {'ll': [77.0, 18.5], 'label': 'DECCAN', 'size': 11}, {'ll': [77.0, 12.9], 'label': 'TAMILAKAM', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [68.403, 36.149], 'label': 'Rabatak', 'date': 'inscription, found 1993', 'acc': True, 'anchor': 'end', 'plate': {'kicker': '9.8 · the Kushans', 'title': 'The Rabatak inscription', 'sub': 'found 1993', 'text': "[[c-rabatak]] [[c-kanishka-date]]", 'sources': ['shiraz-rabatak', 'carc-chronology']}},
    {'ll': [71.578, 34.008], 'label': 'Gandhara', 'date': '(Peshawar)', 'acc': True, 'big': True, 'dy': -10, 'plate': {'kicker': '9.8 · Gandhara', 'title': 'Gandhara', 'sub': 'Buddhist art and texts', 'text': "[[c-gandhara]] [[c-buddha-image]] [[c-bajaur]]", 'sources': ['met-gandhara', 'smarthistory-buddha', 'equinox-bajaur']}},
    {'ll': [77.672, 27.503], 'label': 'Mathura', 'date': 'Kushan Buddha images', 'acc': True, 'big': True, 'dy': 16},
    {'ll': [85.189, 25.598], 'label': 'Pataliputra', 'dy': -8},
    {'ll': [79.81, 11.89], 'label': 'Arikamedu', 'date': 'Indo-Roman port', 'acc': True, 'plate': {'kicker': '9.8 · trade', 'title': 'Arikamedu', 'sub': '1st century CE', 'text': "[[c-arikamedu]]", 'sources': ['efeo-arikamedu']}},
    {'ll': [76.209, 10.156], 'label': 'Pattanam', 'date': 'Muziris?', 'acc': True, 'anchor': 'end', 'plate': {'kicker': '9.8 · trade', 'title': 'Pattanam', 'sub': 'ancient Muziris?', 'text': "[[c-pattanam]]", 'sources': ['muziris-pattanam']}},
    {'ll': [78.119, 9.919], 'label': 'Madurai', 'date': 'Sangam academies (tradition)', 'dy': 16, 'plate': {'kicker': '9.8 · Tamil south', 'title': 'Sangam poetry', 'sub': '1st-4th centuries CE', 'text': "[[c-sangam]] [[c-keeladi]]", 'sources': ['brit-sangam', 'week-keeladi']}}]}]},
 'practice': [
  q("Why does the date of Kanishka matter beyond the list of Kushan kings?",
    ["It proves Gandharan art came before Mathuran art", "Gandharan statues are dated by years of his era", "It fixes when Menander debated the monk Nagasena", "It is given as 78 CE on the Rabatak inscription"], 1,
    "Inscriptions and statues are dated in Kanishka's era, so placing his year 1 in 127 CE rather than earlier moves the whole chronology of Gandharan art.",
    {0: "Which came first is still debated: Alfred Foucher argued for Gandhara, Ananda Coomaraswamy for Mathura.", 2: "Menander ruled about 160-135 BCE, long before Kanishka's era began.", 3: "Rabatak lists the Kushan kings before Kanishka; 78 CE was an older scholarly date, now usually replaced by 127 CE."}),
  q("What best explains the Satavahanas' patronage of both Buddhist and Brahmin institutions?",
    ["Ashoka's edicts urging tolerance between sects", "Wealth from their trade with the Roman world", "Kushan overlords who ruled the Deccan for them", "Pressure from the Sangam poets of Madurai"], 1,
    "The Satavahanas grew rich on trade with the Roman world, and that wealth paid for generous patronage of both Buddhist and Brahmin communities.",
    {0: "Their patronage was paid for by wealth from trade with the Roman world, not by any royal decree.", 2: "The Kushan empire ran from the Oxus to the Ganges; the Deccan was the Satavahanas' own empire.", 3: "The Sangam poems belong to the Tamil kingdoms of the far south, not to the Deccan."})]}

# ---------------------------------------------------------------- 9.9
P9 = {
 'title': "The Gupta age", 'sub': "c. 320-550 CE",
 'lede': "Under the Gupta kings northern India produced Kalidasa's poetry, Aryabhata's astronomy, the first stone temples and the decimal arithmetic that the whole world now uses. Whether to call it a golden age, and for whom, is another matter.",
 'body': [
  "The Guptas rose in the old Magadhan heartland and counted their era from 319/320 CE. [[c-gupta-era]] Samudragupta's court poet boasted of his conquests on an Ashokan pillar, [[c-allahabad]] and his gold coins show a king who was warrior, priest and musician at once. [[c-samudra-coins]] His son Chandragupta II took western India from the Shakas, [[c-cg2]] and was honoured at the cave temples of Udayagiri. [[c-udayagiri]]",
  "Sanskrit literature reached a high point; Kalidasa may have written at his court. [[c-kalidasa]] Aryabhata calculated with decimal place value and argued that the Earth spins. [[c-aryabhata]] When the place-value system with zero began is hotly argued: the Bakhshali manuscript was announced as the oldest example, but its leaves date centuries apart, [[c-bakhshali]] and the first known rules for calculating with zero are Brahmagupta's in 628. [[c-brahmagupta]] Hindu worship moved into permanent stone temples. [[c-deogarh]]",
  "Nationalist historians called this India's golden age; others answer that its glories belonged to a narrow elite while caste rules hardened. [[c-golden-age]] The great law book of caste, the Manusmriti, was probably already a few centuries old. [[c-manu]] Hun invaders from Central Asia took Gandhara around 440. Skandagupta drove back their first attack in the 450s, but around 500-530 their kings Toramana and Mihirakula overran much of the north-west and central India; Gupta power never recovered, and by the mid-6th century the dynasty had faded away. [[c-huns]]",
  {'table': {'head': ["Achievement", "Who or what", "Date"], 'rows': [
    ["Court eulogy on an Ashokan pillar", "Harishena for Samudragupta", "c. 335-375"],
    ["Cave temples: a dated dedication (Cave 6) and a colossal Varaha (Cave 5)", "Udayagiri", "401"],
    ["Decimal place value, pi = 3.1416", "Aryabhata", "c. 499"],
    ["Early stone temple with a tower", "Deogarh", "early 6th century"],
    ["Rules for calculating with zero", "Brahmagupta", "628"]], 'note': "[[c-allahabad]] [[c-udayagiri]] [[c-aryabhata]] [[c-deogarh]] [[c-brahmagupta]]"}}],
 'figure': {'kind': 'chart', 'chart': 'ranges', 'caption': "The Guptas and the date of zero", 'title': "Gupta kings, and the three radiocarbon dates of the Bakhshali manuscript",
  'max': -300, 'min': -1000, 'unit': 'ka', 'ticks': [-300, -400, -500, -600, -700, -800, -900, -1000], 'tickLabels': ['300 CE', '400', '500', '600', '700', '800', '900', '1000 CE'],
  'axis': "years CE", 'hint': "Hover or click a row",
  'marks': [{'ya': -499, 't': 'Aryabhatiya, c. 499'}, {'ya': -628, 't': 'Brahmagupta on zero, 628'}],
  'rows': [
   {'t': 'Samudragupta', 'from': -335, 'to': -375, 'lab': 'c. 335-375', 'acc': True, 'plate': {'kicker': '9.9 · the Guptas', 'title': 'Samudragupta', 'sub': 'c. 335-375', 'text': "[[c-allahabad]] [[c-samudra-coins]]", 'sources': ['epgp-allahabad', 'coinindia-samudra']}},
   {'t': 'Chandragupta II', 'from': -380, 'to': -415, 'lab': 'c. 380-415', 'acc': True, 'plate': {'kicker': '9.9 · the Guptas', 'title': 'Chandragupta II', 'sub': 'c. 380-415', 'text': "[[c-cg2]] [[c-udayagiri]] [[c-kalidasa]]", 'sources': ['brit-cg2', 'map-udayagiri', 'brit-kalidasa']}},
   {'t': 'Alchon Huns in India', 'from': -440, 'to': -528, 'lab': 'c. 440-528', 'open': True, 'plate': {'kicker': '9.9 · the Huns', 'title': 'The Alchon Huns', 'sub': 'from c. 440', 'text': "[[c-huns]]", 'sources': ['rezakhani-huns', 'brit-gupta']}},
   {'t': 'Bakhshali leaf 1', 'sub': 'radiocarbon', 'from': -224, 'to': -383, 'lab': '224-383', 'open': True, 'plate': {'kicker': '9.9 · zero', 'title': 'The Bakhshali manuscript', 'sub': 'three leaves, three dates', 'text': "[[c-bakhshali]] [[c-brahmagupta]]", 'sources': ['ox-bakhshali', 'indology-bakhshali', 'hssa-bakhshali']}},
   {'t': 'Bakhshali leaf 2', 'sub': 'radiocarbon', 'from': -680, 'to': -779, 'lab': '680-779', 'open': True},
   {'t': 'Bakhshali leaf 3', 'sub': 'radiocarbon', 'from': -885, 'to': -993, 'lab': '885-993', 'open': True}]},
 'practice': [
  q("What do the Bakhshali radiocarbon results actually establish?",
    ["That zero as a number was first used in the 3rd century", "That its leaves span centuries, leaving its date open", "That each leaf was copied in the 3rd or 4th century CE", "That peer review confirmed the Bodleian's early date"], 1,
    "The three tested leaves gave 224-383, 680-779 or 790-868, and 885-993 CE; Kim Plofker, Dominik Wujastyk and colleagues argue that the latest leaf dates the copying.",
    {0: "Only one leaf dates that early, and the first text to treat zero as a number is Brahmagupta's of 628.", 2: "The three leaves gave very different dates, the latest 885-993 CE.", 3: "Critics faulted the Bodleian for announcing the results by press release without peer review."}),
  q("Why do historians read Samudragupta's Allahabad pillar eulogy with caution?",
    ["It is Ashoka's own text, reused for a Gupta king", "It is a court poet's praise, not a record", "It is in the Bactrian language, in Greek letters", "It describes defeats by the Huns, not victories"], 1,
    "His court poet Harishena wrote it; its claims, as one specialist puts it, 'can hardly be taken in their face value'.",
    {0: "Only the pillar is Ashokan; the eulogy was written by Samudragupta's court poet Harishena.", 2: "That describes the Kushan Rabatak inscription (9.8), not a Gupta court poem.", 3: "It lists kings 'uprooted' and 'captured'; the Huns came from about 440, after Samudragupta's reign."})]}

# ---------------------------------------------------------------- 9.10
P10 = {
 'title': "Buddhism travels", 'sub': "to Sri Lanka, Central Asia and China",
 'lede': "Buddhism was one of the first religions to spread far beyond the culture that produced it. Carried by monks and merchants along the land and sea routes of 9.5 and 8.11, it reached China by the 1st century CE, and by 400 Chinese monks were walking to India to fetch better texts.",
 'body': [
  "Sri Lanka's chronicles credit Ashoka's own son with bringing Buddhism to the island, [[c-mahinda]] and it has been a Buddhist land ever since. In Central Asia, oasis cities on the routes north and south of the Taklamakan built monasteries and cave temples.",
  "In China the earliest firm record is an imperial edict of 65 CE about a prince who honoured the Buddha. [[c-liuying]] The famous story of an emperor's dream and a mission to India is a later legend. [[c-mingdi]] Translation began in earnest with An Shigao, a Parthian, in Luoyang, [[c-anshigao]] and reached its peak with Kumarajiva, who arrived in Chang'an in 401. [[c-kumarajiva]] Some early 'Buddhist' carvings in China may be much later than once thought. [[c-kongwangshan]]",
  "In 399 the monk Faxian set out to find complete monastic rules. He crossed the deserts and mountains to India, stayed years in the Ganges valley and in Sri Lanka, and came home by sea. [[c-faxian]] His record is one of our best descriptions of Gupta India. By the 5th century Chinese rulers were sponsoring vast cave temples at Dunhuang and Yungang. [[c-mogao]] [[c-yungang]]",
  {'table': {'head': ["Who", "From", "To", "When"], 'rows': [
    ["Mahinda (tradition)", "Ashoka's India", "Sri Lanka", "c. 250 BCE"],
    ["An Shigao", "Parthia", "Luoyang", "c. 148-170 CE"],
    ["Kumarajiva", "Central Asia", "Chang'an", "arrived 401"],
    ["Faxian", "China", "India and Sri Lanka, and back", "399-c. 412"]], 'note': "[[c-mahinda]] [[c-anshigao]] [[c-kumarajiva]] [[c-faxian]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 96.0, 'lat': 16.0, 'zoom': 4.6}, 'caption': "Faxian's journey, 399-c. 412 CE", 'hint': "Click a place",
  'legend': [['acc dash', 'Faxian, out by land (simplified)'], ['dash', 'home by sea (simplified)'], ['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'route', 'items': [{'path': [[108.929, 34.258], [103.8, 36.1], [98.5, 39.7], [94.683, 40.167], [88.0, 39.0], [79.934, 37.109], [75.987, 39.467], [73.5, 36.5], [71.578, 34.008], [75.0, 31.0], [77.672, 27.503], [81.0, 26.0], [85.189, 25.598], [84.987, 24.698]], 'label': 'out by land, 399-402', 'lab': [84.0, 36.5], 'ldy': 20, 'acc': True, 'head': True}]},
   {'type': 'route', 'items': [{'path': [[85.189, 25.598], [88.0, 22.0], [86.0, 15.0], [82.0, 9.0], [80.413, 8.312], [86.0, 6.0], [95.0, 5.5], [100.0, 3.0], [104.5, 1.3], [107.0, -4.5], [109.0, 1.0], [112.0, 12.0], [117.0, 22.5], [121.5, 29.5], [121.0, 33.0], [120.631, 36.181]], 'label': 'home by sea, c. 411-412', 'lab': [112.0, 12.0], 'ldy': 16, 'head': True}]},
   {'type': 'region', 'items': [{'ll': [84.0, 39.0], 'label': 'TAKLAMAKAN', 'size': 9}, {'ll': [110.0, 30.0], 'label': 'CHINA', 'size': 12}, {'ll': [79.0, 21.0], 'label': 'GUPTA INDIA', 'size': 11}]},
   {'type': 'points', 'items': [
    {'ll': [112.437, 34.673], 'label': 'Luoyang', 'acc': True, 'big': True, 'dy': -10, 'plate': {'kicker': '9.10 · China', 'title': 'Buddhism reaches China', 'sub': '1st-2nd centuries CE', 'text': "[[c-liuying]] [[c-mingdi]] [[c-anshigao]]", 'sources': ['palumbo2007', 'iias-anshigao']}},
    {'ll': [108.929, 34.258], 'label': "Chang'an", 'date': 'Kumarajiva, 401', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '9.10 · translators', 'title': 'Kumarajiva', 'sub': '344-413', 'text': "[[c-kumarajiva]]", 'sources': ['brit-kumarajiva']}},
    {'ll': [94.683, 40.167], 'label': 'Dunhuang', 'date': 'Mogao caves from 366', 'acc': True, 'dy': -10, 'plate': {'kicker': '9.10 · cave temples', 'title': 'Mogao and Yungang', 'sub': '4th-6th centuries', 'text': "[[c-mogao]] [[c-yungang]]", 'sources': ['unesco-mogao', 'unesco-yungang']}},
    {'ll': [113.13, 40.11], 'label': 'Yungang', 'date': '5th-6th century caves', 'dy': -8},
    {'ll': [79.934, 37.109], 'label': 'Khotan', 'dy': 16},
    {'ll': [71.578, 34.008], 'label': 'Gandhara', 'anchor': 'end', 'dy': -6},
    {'ll': [85.189, 25.598], 'label': 'Pataliputra', 'date': "Faxian's long stay", 'acc': True, 'big': True, 'dy': -10, 'plate': {'kicker': '9.10 · Faxian', 'title': 'Faxian', 'sub': '399 to c. 412', 'text': "[[c-faxian]]", 'sources': ['brit-faxian']}},
    {'ll': [84.987, 24.698], 'label': 'Bodh Gaya', 'anchor': 'end', 'dy': 14},
    {'ll': [80.413, 8.312], 'label': 'Anuradhapura', 'date': 'Mahinda (tradition)', 'acc': True, 'anchor': 'end', 'plate': {'kicker': '9.10 · Sri Lanka', 'title': 'Anuradhapura', 'sub': 'c. 250 BCE (tradition)', 'text': "[[c-mahinda]]", 'sources': ['so-mahinda', 'brit-mahavamsa']}},
    {'ll': [119.216, 34.598], 'label': 'Kongwangshan', 'dy': 16, 'plate': {'kicker': '9.10 · art', 'title': 'Kongwangshan', 'sub': 'Han or 6th century?', 'text': "[[c-kongwangshan]]", 'sources': ['yale-kongwangshan']}},
    {'ll': [120.631, 36.181], 'label': 'Shandong', 'date': 'Faxian lands', 'dy': -8}]}]},
 'practice': [
  q("Why do historians prefer the edict of 65 CE to the story of Emperor Ming's dream as the start of Chinese Buddhism?",
    ["It is carved at the White Horse Temple in Luoyang", "It dates from its own time; the dream is legend", "It was written by the Parthian translator An Shigao", "Maspero proved Ming's envoys really reached India"], 1,
    "The edict praising Liu Ying is the earliest firm evidence. Henri Maspero showed the dream story to be a pious legend, and Antonello Palumbo argues the mission to India was added by later editors.",
    {0: "The founding of the White Horse Temple is part of the legend of Ming's dream.", 2: "An Shigao worked in Luoyang from about 148, some eighty years after the edict.", 3: "Maspero showed in 1910 that the story 'bears all the traits of a pious legend'."}),
  q("What does Faxian's route show about how Buddhism moved?",
    ["It moved overland, through Central Asia's oases", "Land routes and sea lanes both linked India and China", "It moved by sea from Sri Lanka, not over the deserts", "It moved through missions sent by the Gupta kings"], 1,
    "He went out across Central Asia to India in 399 and came home by sea, by way of Sri Lanka and South-East Asia.",
    {0: "He came home by sea, by way of Sri Lanka and South-East Asia.", 2: "He went out overland, across the deserts and mountains of Central Asia.", 3: "Faxian was a Chinese monk who went to India to find monastic rules, not a Gupta envoy."})]}

# ---------------------------------------------------------------- 9.11
P11 = {
 'title': "Han and Rome compared", 'sub': "two empires at the two ends of Eurasia",
 'lede': "Around 100 CE two empires of similar size and population ruled the two ends of Eurasia. They knew almost nothing of each other. Comparing them is one of the liveliest fields in history, and the biggest question is not why they fell but why one came back and the other never did.",
 'body': [
  "The similarities are striking. Each covered about 4 million square kilometres and held some 60 million people. [[c-size-similar]] A 2025 study finds that income was about as unequally shared in both, though the Han elite took a larger share. [[c-inequality2025]] Both, by modern standards, taxed lightly. [[c-low-tax]]",
  "The differences are in how they governed. The Han ran a bureaucracy of some 120,000-130,000 salaried officials, recorded in the dynastic history; [[c-han-officials]] Rome made do with about 600 senators and perhaps 20,000 knights, leaning on cities to govern themselves. [[c-rome-elite]] One historian sums it up as soldiers versus scholar-officials. [[c-loewe]] Rome spent far more on its standing army; [[c-roman-army]] the Han spent a much larger share of its defence budget paying foreign peoples to keep the peace. [[c-low-tax]] Even their money differed: China's coins were bronze tokens, Rome's were precious metal. [[c-coins-compare]]",
  "Both empires broke up, the Han in 220 and the western Roman empire in the 5th century. China was briefly reunited under the Jin in 280 and lastingly under the Sui in 589, and again and again afterwards, while no one ever rebuilt the Roman world. Walter Scheidel argues that this 'First Great Divergence' shaped the whole later history of the world, because a Europe of competing states could innovate as no single empire would. [[c-divergence]]",
  {'table': {'head': ["", "Han China", "Roman empire"], 'rows': [
    ["Area", "about 4 million km²", "about 4 million km²"],
    ["People", "57.7-59.6 million registered (census, 2 CE)", "about 60-75 million (estimates, 2nd century; see 8.10)"],
    ["Gini coefficient (estimate)", "0.48", "0.46"],
    ["Top 1% share of income (estimate)", "26%", "19%"],
    ["Central officials", "about 120,000-130,000 (Han history)", "c. 600 senators, c. 20,000 equestrians"],
    ["Coinage", "cast bronze wuzhu", "struck gold, silver and bronze"],
    ["After the fall", "briefly reunited 280; lastingly 589", "never reunified"]], 'note': "[[c-size-similar]] [[c-inequality2025]] [[c-han-officials]] [[c-rome-elite]] [[c-coins-compare]] [[c-divergence]]"}}],
 'figure': {'kind': 'chart', 'chart': 'ledger', 'signs': False, 'caption': "Two empires, two ways of ruling", 'title': "Han China and the Roman empire, 1st-2nd centuries CE",
  'left': {'h': 'Han China', 'items': [
   {'t': 'About 58-60 million registered people', 's': 'census of 2 CE'},
   {'t': 'Some 120,000-130,000 officials on the books', 's': 'Han history'},
   {'t': 'Top 1% take about 26% of income', 's': 'Alfani, Bolla and Scheidel (2025)'},
   {'t': 'Bronze coins, cast by the state', 's': 'the wuzhu, from 118 BCE'},
   {'t': 'Reunited in 280 and, lastingly, in 589', 's': 'Scheidel'}]},
  'right': {'h': 'The Roman empire', 'items': [
   {'t': 'Perhaps 60-75 million people', 's': 'modern estimates'},
   {'t': 'About 600 senators and 20,000 equestrians', 's': 'Scheidel and Friesen (2009)'},
   {'t': 'Top 1% take about 19% of income', 's': 'Alfani, Bolla and Scheidel (2025)'},
   {'t': 'Gold and silver coins, struck', 's': 'the aureus and denarius'},
   {'t': 'Never rebuilt after the 5th century', 's': "Scheidel's 'First Great Divergence'"}]},
  'notes': ["All income figures are model-based estimates."]},
 'practice': [
  q("According to the 2025 study by Alfani, Bolla and Scheidel, how did Han and Roman inequality compare?",
    ["Rome was a little more unequal, with a Gini of 0.48 to 0.46", "The Han were a little more unequal, with a richer top 1%", "They were alike, with top 1% shares of about 26% in both", "They were alike, according to both empires' tax registers"], 1,
    "Gini 0.48 for the Han in 2 CE against 0.46 for Rome in about 165 CE; the top 1 percent took about 26 percent of income in Han China and 19 percent in Rome.",
    {0: "The figures are the other way round: Rome's estimated Gini was 0.46, the Han's 0.48.", 2: "Rome's top 1 percent took about 19 percent, against 26 percent in Han China.", 3: "The figures are model-based, reconstructed from urbanisation and population density, not from tax records."}),
  q("Which argument fits Walter Scheidel's 'First Great Divergence'?",
    ["Rome fell because its population was smaller than Han China's", "China kept reuniting, Rome never did, and that shaped Europe", "Europe's later growth came despite its divisions, not from them", "Both empires collapsed because they taxed their people too hard"], 1,
    "He turns 'why did Rome fall?' into 'why did it never come back?', and argues that Europe's lasting fragmentation was 'an indispensable precondition' for its later growth.",
    {0: "The two populations were of similar size, some 60 million or more each.", 2: "Scheidel argues the reverse: fragmentation was 'an indispensable precondition' for Europe's later growth.", 3: "Scheidel classes both as 'low-tax regimes'."})]}

PAGES = [P8, P9, P10, P11]
