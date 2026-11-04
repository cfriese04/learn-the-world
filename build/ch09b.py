# Chapter 9, pages 9.4 to 9.7. Coordinates are [longitude, latitude].
from common import c, q

S = {
 # 9.4
 'cu-saltiron': ("Columbia University, Asia for Educators, \"A record of the Debate on Salt and Iron\" (from de Bary and Bloom, Sources of Chinese Tradition, 1999)", "https://afe.easia.columbia.edu/main_pop/ps//ps_china-debate-salt-iron.htm"),
 'wagner-iron': ("Donald B. Wagner, \"Technology as seen through the case of ferrous metallurgy in Han China\"", "https://donwagner.dk/EncIt/EncIt.html"),
 'brit-han': ("Encyclopaedia Britannica, \"History of China: the Han dynasty\"", "https://www.britannica.com/topic/history-of-China/The-Han-dynasty"),
 'wang2024': ("Wang, Liu, Pollard et al., lead isotopes in Han bronze mirrors, Archaeological and Anthropological Sciences 16 (2024)", "https://link.springer.com/article/10.1007/s12520-024-02016-2"),
 'zhang2020': ("Zhang et al., \"Iron production and trading in Lingnan during the Qin and Han dynasties\", Antiquity 94 (2020)", "https://www.cambridge.org/core/journals/antiquity/article/iron-production-and-trading-in-lingnan-during-the-qin-and-han-dynasties/9EB822B1E9CE3B15A1DB1B6AC54B7970"),
 'rom-wuzhu': ("Royal Ontario Museum, on the wuzhu coin", "https://rom.on.ca/en/node/5474"),
 'bm-wuzhu': ("British Museum, wuzhu coin 1982,0628.2 (Google Arts & Culture)", "https://artsandculture.google.com/asset/wuzhu-coin-issued-by-emperor-xuandi/6wH3PKoXR06Xxg?hl=en"),
 'smith-wangmang': ("Smithsonian Magazine, \"Emperor Wang Mang: China's first socialist?\"", "https://www.smithsonianmag.com/history/emperor-wang-mang-chinas-first-socialist-2402977/"),
 'ox-paper': ("History of Science Museum, Oxford, \"Origins of paper\"", "https://www.cabinet.ox.ac.uk/node/7013"),
 'xinhua-fangmatan': ("Xinhua, on the Fangmatan paper fragment (29 November 2016)", "https://www.xinhuanet.com/english/2016-11/29/c_135867579.htm"),
 # 9.5
 'brit-maodun': ("Encyclopaedia Britannica, \"Maodun\"", "https://www.britannica.com/biography/Maodun"),
 'brit-xiongnu': ("Encyclopaedia Britannica, \"Xiongnu\"", "https://www.britannica.com/topic/Xiongnu"),
 'brit-wudi': ("Encyclopaedia Britannica, \"Wudi\" (emperor of the Han dynasty)", "https://www.britannica.com/biography/Wudi-emperor-of-Han-dynasty"),
 'benjamin2018': ("Craig Benjamin, Empires of Ancient Eurasia (Cambridge, 2018), ch. 3, \"Zhang Qian and Han expansion into Central Asia\"", "https://www.cambridge.org/core/books/abs/empires-of-ancient-eurasia/zhang-qian-and-han-expansion-into-central-asia/B9352627ADD0B8E5FCB3EA13C7DF7B04"),
 'brit-zhangqian': ("Encyclopaedia Britannica, \"Zhang Qian\"", "https://www.britannica.com/biography/Zhang-Qian"),
 'brit-greatwall-han': ("Encyclopaedia Britannica, \"Great Wall of China: the Han through Yuan dynasties\"", "https://www.britannica.com/topic/Great-Wall-of-China/The-Han-through-Yuan-dynasties"),
 'unesco-silkroads': ("UNESCO World Heritage Centre, \"Silk Roads: the Routes Network of Chang'an-Tianshan Corridor\"", "https://whc.unesco.org/en/list/1442"),
 'cd-xuanquan2023': ("China Daily, \"Reviving the glory of millennia-old posthouse ruins in Dunhuang\" (10 August 2023)", "https://govt.chinadaily.com.cn/s/202308/10/WS64d44147498ea274927c7d30/reviving-the-glory-of-millennia-old-posthouse-ruins-in-dunhuang.html"),
 'cd-xuanquan2025': ("China Daily, on the Xuanquanzhi site (18 April 2025)", "https://www.chinadaily.com.cn/a/202504/18/WS68020399a3104d9fd3820446.html"),
 'mertens2019': ("Matthias Mertens, \"Did Richthofen really coin 'the Silk Road'?\", The Silk Road 17 (2019)", "https://edspace.american.edu/silkroadjournal/wp-content/uploads/sites/984/2020/02/2-Mertens-Did-Richthofen-Really-Coin-the-Silk-Road.pdf"),
 'whitfield-tarim': ("Susan Whitfield, \"On the Silk Road: trade in the Tarim?\" (University of East Anglia repository)", "https://ueaeprints.uea.ac.uk/76586/1/Whitfield_TradeTarim.pdf"),
 'sd-xiongnu2023': ("ScienceDaily, on Lee, Miller, Jeong et al., ancient DNA of the Xiongnu, Science Advances 9 (2023)", "https://sciencedaily.com/releases/2023/04/230414201820.htm"),
 # 9.6
 'brit-magadha': ("Encyclopaedia Britannica, \"India: Magadhan ascendancy\"", "https://www.britannica.com/place/India/Magadhan-ascendancy"),
 'brit-megasthenes': ("Encyclopaedia Britannica, \"Megasthenes\"", "https://www.britannica.com/biography/Megasthenes"),
 'arrian-indica10': ("Arrian, Indica 10, quoting Megasthenes on Pataliputra (translation at Sententiae Antiquae)", "https://sententiaeantiquae.com/tag/pataliputra/"),
 'strabo15': ("Strabo, Geography 15.1.36 (Loeb translation on LacusCurtius)", "https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Strabo/15A2*.html"),
 'patra-jaugada': ("Benudhar Patra, 'Jaugada: an early historical fort town of Orissa', Orissa Review (January 2007)", "https://magazines.odisha.gov.in/orissareview/jan-2007/engpdf/44-47.pdf"),
 'brit-ashoka-succ': ("Encyclopaedia Britannica, \"India: Ashoka and his successors\"", "https://www.britannica.com/place/India/Ashoka-and-his-successors"),
 'organiser-kumrahar': ("Organiser, on the ASI re-exposing the Mauryan pillared hall at Kumrahar (4 December 2024)", "https://www.organiser.org/2024/12/04/267840/bharat/uncovering-the-past-asi-begins-historic-excavation-of-mauryan-empires-assembly-hall-in-patna/"),
 'dh-kumrahar': ("Deccan Herald, on the buried Mauryan hall at Kumrahar (29 October 2023)", "https://www.deccanherald.com/amp/story/india%2Fbihar%2Farchaeologists-flag-concern-over-buried-mauryan-period-assembly-hall-demand-immediate-restoration-2746910"),
 'trautmann1968': ("Thomas R. Trautmann, The Structure and Composition of the Kautiliya Arthasastra (SOAS PhD, 1968)", "https://soas-repository.worktribe.com/output/400931/the-structure-and-composition-of-the-kautiliya-arthasastra"),
 'mcclish2019': ("Mark McClish, The History of the Arthaśāstra (Cambridge, 2019), front matter", "https://assets.cambridge.org/97811084/76904/frontmatter/9781108476904_frontmatter.pdf"),
 'olivelle2013': ("Patrick Olivelle, King, Governance, and Law in Ancient India: Kauṭilya's Arthaśāstra (Oxford, 2013)", "https://academic.oup.com/book/8486"),
 # 9.7
 'dhammika-edicts': ("S. Dhammika, The Edicts of King Asoka (Buddhist Publication Society, 1993), at Access to Insight", "https://accesstoinsight.org/lib/authors/dhammika/wheel386.html"),
 'unesco-shahbazgarhi': ("UNESCO Tentative List, \"Shahbazgarhi Rock Edicts\"", "https://whc.unesco.org/en/tentativelists/1880"),
 'lhi-kandahar': ("LiveHistoryIndia, \"Ashoka's Kandahar edicts: an emperor's message to the world\"", "https://livehistoryindia.com/story/eras/ashoka-s-kandahar-edicts-an-emperor-s-message-to-the-world"),
 'dhammika-prinsep': ("S. Dhammika, \"Prinsep discovers Ashoka\" (2012)", "https://smallpdfs.buddhistuniversity.net/dhammika_2012_prinsep-discovers-ashoka.pdf"),
 'open-olivelle': ("Upinder Singh, review of Patrick Olivelle, Ashoka: Portrait of a Philosopher King (2023), Open (November 2023)", "https://openthemagazine.com/lounge/books/ashoka-the-king-who-said-sorry"),
 'brit-shunga': ("Encyclopaedia Britannica, \"Shunga dynasty\"", "https://www.britannica.com/topic/Shunga-dynasty"),
 'pwc-mauryan-decline': ("P. Singh, \"Decline of the Mauryan empire\", Patna Women's College teaching notes", "https://patnawomenscollege.in/?p=53762"),
 'coningham1996': ("Coningham, Allchin, Batt and Lucy, 'Passage to India? Anuradhapura and the early use of the Brahmi script', Cambridge Archaeological Journal 6 (1996)", "https://www.cambridge.org/core/journals/cambridge-archaeological-journal/article/abs/passage-to-india-anuradhapura-and-the-early-use-of-the-brahmi-script/DAAA2514FB08E1DDE3FAFF2171AB097B"),
 'knaw-schmid': ("Charlotte Schmid, The Aśokan Breakthrough, Gonda Lecture (KNAW, 2024)", "https://knaw.nl/en/publications/asokan-breakthrough"),
 'print-bahaj2025': ("ThePrint, \"Brahmi script existed in India way before Ashoka edicts: ASI paper\" (4 November 2025)", "https://theprint.in/feature/brahmi-script-existed-in-india-way-before-ashoka-edicts-asi-paper/2776884"),
}

C = {
 # 9.4
 'c-saltiron-debate': c("In 81 BCE the court held a debate between officials led by Sang Hongyang and Confucian 'literati' over Emperor Wu's state monopolies on salt, iron and liquor and his system of state trading to even out prices.", 'consensus', ['cu-saltiron', 'wagner-iron'], show=False),
 'c-literati-case': c("The literati argued that monopolies taught the people to chase profit and drew them from farming: 'Never should material profit appear as a motive of government.'", 'consensus', ['cu-saltiron'], show=False),
 'c-sang-case': c("Sang Hongyang replied that the monopolies paid for defence against the Xiongnu and kept prices steady: 'Abolition of these measures is not expedient!'", 'consensus', ['cu-saltiron'], show=False),
 'c-yantielun': c("The record of the debate, the Yantie lun, was compiled afterwards, between 74 and 49 BCE, by the scholar Huan Kuan.", 'approx', ['wagner-iron', 'cu-saltiron'], "It is a literary reconstruction, not a transcript; how evenly it presents the officials' case is a matter of judgement."),
 'c-iron-monopoly': c("The iron monopoly began about 119-110 BCE; by 2 CE there were 48 Iron Offices running large blast-furnace works.", 'approx', ['wagner-iron', 'brit-han', 'wang2024', 'zhang2020'], "Sources give dates from about 119 to 110 BCE for the start (Wagner and Britannica: about 117). Donald Wagner's rough estimate of about 5,000 tonnes of legal iron a year is one to which, he says, 'one cannot lend much credence'."),
 'c-iron-critics': c("Critics complained that state-made tools were 'crude and coarse' and expensive.", 'debated', ['wagner-iron'], "Wagner thinks most of the criticism came from provincial agricultural interests, not from the iron industry, so the complaints are not neutral reports."),
 'c-monopoly-swings': c("The monopolies were abolished in 44 BCE and restored three years later, revived again in 85 CE and dropped in 88; by the later 1st century CE much of the industry was private.", 'consensus', ['wagner-iron', 'brit-han'], show=False),
 'c-monopoly-reach': c("Archaeology suggests the monopoly's reach was patchy: a 2024 lead-isotope study of Han mirrors finds it touched mirror lead less than other bronzes, and the far south seems to have imported most of its iron.", 'debated', ['wang2024', 'zhang2020'], "New. These are inferences from metal chemistry and site surveys, tested against the claims of the texts."),
 'c-wuzhu': c("Emperor Wu introduced the wuzhu ('five zhu') coin in 118 BCE; it stayed in use, in one form or another, for about 700 years.", 'consensus', ['rom-wuzhu', 'bm-wuzhu', 'brit-han'], show=False),
 'c-han-tax': c("Han farmers paid a land tax in kind of one-thirtieth of the harvest (sometimes one-fifteenth) and a poll tax in cash; men also owed a month of labour a year and two years of military service.", 'consensus', ['brit-han'], show=False),
 'c-great-families': c("Under the Eastern Han great landowning families came to dominate local office, manipulate tax and census registers and keep armed retainers on their estates.", 'consensus', ['brit-han'], show=False),
 'c-census2': c("The census of 2 CE recorded 12,233,000 households and 59,595,000 people.", 'approx', ['brit-han'], "These are registered people only; the true population was probably somewhat larger."),
 'c-wangmang': c("Wang Mang, who seized the throne in 9 CE, tried to abolish private landownership and the private slave trade and issued new kinds of coin; the reforms failed against fierce opposition, and he was killed in 23 CE.", 'debated', ['brit-han', 'smith-wangmang'], "What he was trying to do is disputed: Hu Shih (1928) called him a 'socialist emperor'; Homer Dubs and Hans Bielenstein saw a Confucian restorer, and Bielenstein blamed Yellow River floods for his fall."),
 'c-cailun': c("The Han history records that the court official Cai Lun presented a method of making paper in 105 CE, but archaeology has found paper more than a century older.", 'consensus', ['brit-han', 'ox-paper'], show=False),
 'c-fangmatan': c("A fragment found at Fangmatan in Gansu in 1986, with a map drawn on it, has been dated to the Western Han, perhaps 250 years before Cai Lun.", 'debated', ['xinhua-fangmatan'], "Li Xiaocen accepts it as paper made by a different process; Chen Gang of Fudan University says it needs more study before it counts as true paper."),
 # 9.5
 'c-maodun': c("Under Maodun (ruled about 209-174 BCE) the Xiongnu of the Mongolian steppe became a great power.", 'approx', ['brit-maodun'], "His dates come from Sima Qian."),
 'c-heqin': c("Until about 135 BCE the early Han emperors bought peace with the Xiongnu by sending gold, silk and princesses as brides, a policy called heqin, 'peace through kinship'.", 'consensus', ['brit-han', 'brit-xiongnu'], show=False),
 'c-wu-wars': c("Emperor Wu (reigned 141-87 BCE) went on the attack from 133 BCE; his wars pushed the Xiongnu back but exhausted the treasury, and his campaigns beyond the Gobi failed to destroy them.", 'consensus', ['brit-wudi', 'brit-han', 'benjamin2018'], show=False),
 'c-ferghana': c("Han armies marched to Ferghana in 104 BCE and failed, then returned in 101 BCE and brought back its famous 'blood-sweating' horses.", 'consensus', ['brit-wudi'], show=False),
 'c-zhangqian': c("Zhang Qian set out in 138 BCE to find the Yuezhi, enemies of the Xiongnu; he was held by the Xiongnu for about ten years, reached the Yuezhi in Bactria, and returned after some thirteen years with the first Chinese reports of Central Asia.", 'approx', ['brit-zhangqian', 'benjamin2018'], "The dates of his return and second mission are approximate; he died in 114 BCE."),
 'c-hexi-wall': c("From 121 BCE the Han built walls and beacon towers through the Hexi corridor, 'a beacon every 5 li, a tower every 10 li', reaching Dunhuang by about 100 BCE.", 'approx', ['brit-greatwall-han', 'brit-han'], "The quoted standard comes from documents found at Juyan; the completion date is approximate."),
 'c-silkroads-unesco': c("UNESCO lists the Chang'an-Tianshan corridor of the Silk Roads, a network that took shape between the 2nd century BCE and the 1st century CE.", 'consensus', ['unesco-silkroads'], show=False),
 'c-xuanquan': c("The relay station at Xuanquanzhi, about 64 km from Dunhuang, was used for about 400 years; excavated in 1990-92, it yielded more than 70,000 objects, including inscribed wooden slips, silk and paper.", 'consensus', ['cd-xuanquan2023', 'cd-xuanquan2025'], show=False),
 'c-xuanquan-slips': c("Its slips record the station hosting up to 1,074 guests when a delegation from Khotan passed through, and the envoy Chang Hui on his way west in 65 BCE, and list more than 80 relay stations between Chang'an and Dunhuang.", 'consensus', ['cd-xuanquan2023'], show=False),
 'c-silkroad-term': c("The name 'Silk Road' is a 19th-century German coinage, popularised by Ferdinand von Richthofen in 1877 but used earlier by Carl Ritter and others.", 'consensus', ['mertens2019'], show=False),
 'c-silkroad-trade': c("How much trade the routes carried is disputed.", 'debated', ['whitfield-tarim'], "Valerie Hansen argues the volume was small and mostly local, and that the prosperity of the north-west came from state spending on garrisons; Susan Whitfield accepts the low volume but argues that high-value long-distance trade mattered: 'Volume is only part of the story.'"),
 'c-xiongnu-dna': c("Ancient DNA published in 2023 shows the Xiongnu were genetically very diverse, a multiethnic empire; elite burials had more eastern Eurasian ancestry, and high-status frontier graves were disproportionately women's.", 'approx', ['sd-xiongnu2023'], "New. The results come from cemeteries in Mongolia and may not represent the whole empire."),
 'c-xiongnu-split': c("The Xiongnu split in 51 BCE and the eastern branch submitted to the Han; a link between the Xiongnu and the later Huns is possible but unproven.", 'debated', ['brit-xiongnu'], "The Hun connection rests on names and some shared customs, not on clear evidence of descent."),
 # 9.6
 'c-nandas': c("The Nanda kings, of low birth according to tradition, ruled Magadha in the 4th century BCE and were famous for their wealth, probably from a regular land revenue.", 'tradition', ['brit-magadha'], "Their origins and dates come from later Indian, Buddhist and Greek accounts."),
 'c-chandragupta': c("Chandragupta Maurya (reigned about 321-297 BCE) overthrew the Nandas and founded the first empire to cover most of the Indian subcontinent.", 'approx', ['brit-magadha'], "His dates are reconstructed from Greek synchronisms."),
 'c-seleucus': c("After a war in about 305 BCE, Alexander's successor Seleucus I ceded his lands west of the Indus to Chandragupta in exchange for 500 war elephants, and the two kings exchanged envoys.", 'approx', ['brit-magadha'], "Some accounts date the treaty to about 303 BCE."),
 'c-megasthenes': c("Seleucus' envoy Megasthenes wrote a four-book Indica, now lost; it survives only in quotations by later Greek and Roman writers, and contains errors and idealised pictures of India.", 'consensus', ['brit-megasthenes'], show=False),
 'c-pataliputra-arrian': c("As quoted by Arrian, Megasthenes described the capital Pataliputra as 80 by 15 stades (roughly 15 by 3 km), ringed by a ditch about thirty cubits deep, with 570 towers and 64 gates; Strabo adds that its wall was of wood, pierced for archers.", 'tradition', ['arrian-indica10', 'strabo15'], "A lost eyewitness account known only through a later writer; the figures cannot be checked."),
 'c-pataliputra-gov': c("Pataliputra, under modern Patna, grew from a fort built by Ajatashatru; Megasthenes says a board of 30 officials in six committees ran the city.", 'tradition', ['brit-magadha', 'brit-ashoka-succ'], "The city's site is certain; the committee system comes from Megasthenes alone."),
 'c-kumrahar': c("At Kumrahar in Patna excavators in 1912-15 and 1951-55 found a hall of 80 stone pillars; reburied in 2004 because of waterlogging, it began to be re-exposed by the Archaeological Survey of India in December 2024.", 'consensus', ['organiser-kumrahar', 'dh-kumrahar'], show=False),
 'c-kumrahar-council': c("Some identify the Kumrahar hall as the place where Ashoka held the Third Buddhist Council.", 'debated', ['organiser-kumrahar'], "A popular identification without direct evidence."),
 'c-arthashastra-date': c("The Arthashastra, a Sanskrit treatise on statecraft and economics, has been dated anywhere from the 4th century BCE to the 3rd century CE.", 'debated', ['brit-magadha', 'olivelle2013'], "Most authorities place its core in the early Mauryan period but think much of the surviving text is later; Patrick Olivelle dates the surviving work to the first centuries CE."),
 'c-arthashastra-authors': c("Statistical study of its vocabulary suggests different books were written by different authors, and that the text was later reworked to fit Brahmin religious law.", 'debated', ['trautmann1968', 'mcclish2019'], "Thomas Trautmann (1968) found at least three authors but still thought Kautilya real; Mark McClish (2019) argues a practical treatise was later given a Brahmanical frame."),
 'c-kautilya': c("Tradition makes its author Kautilya, also called Chanakya, Chandragupta's chief minister.", 'tradition', ['brit-magadha'], "Britannica calls the identification 'contested'."),
 # 9.7
 'c-ashoka-dates': c("Ashoka, Chandragupta's grandson, came to the throne in about 268 BCE and attacked Kalinga, on India's east coast, about eight years later.", 'approx', ['brit-ashoka-succ', 'dhammika-edicts'], "His accession is dated 272, 268 or about 265 BCE and his death 238 or 232; Britannica's biography gives c. 265-238 or c. 273-232."),
 'c-re13': c("In his Rock Edict 13 Ashoka says that in the Kalinga war 'one hundred and fifty thousand were deported, one hundred thousand were killed and many more died', and that he now regards 'conquest by Dhamma' as the best conquest.", 'approx', ['dhammika-edicts'], "The words are certain; the numbers are the king's own and cannot be checked."),
 'c-re13-absent': c("At Dhauli and Jaugada, in Kalinga itself, Rock Edicts 11-13, including the edict of remorse, were left out, and two special 'Separate Edicts' addressed to local officials were carved instead.", 'consensus', ['patra-jaugada', 'dhammika-edicts'], show=False),
 'c-edict-sites': c("Ashoka's edicts survive at more than 30 sites across India, Nepal, Pakistan and Afghanistan, carved on rocks and polished stone pillars.", 'consensus', ['dhammika-edicts'], show=False),
 'c-edict-scripts': c("Most are in Prakrit in the Brahmi script; in the north-west they use Kharosthi, written right to left, and near Kandahar Greek and Aramaic.", 'consensus', ['brit-ashoka-succ', 'dhammika-edicts', 'unesco-shahbazgarhi'], show=False),
 'c-kandahar-edict': c("A bilingual Greek and Aramaic edict found at Kandahar in 1958 announces that the king has abstained from killing living beings; its cast was stolen when the Kabul Museum was looted in 1992-94, and the original's whereabouts are unknown.", 'consensus', ['lhi-kandahar'], show=False),
 'c-prinsep': c("In 1837 James Prinsep deciphered Brahmi and read a pillar edict of 'Beloved-of-the-Gods, King Piyadasi'; the king was later identified with the Ashoka of Buddhist chronicles, and an edict found in 1915 names him as Asoka.", 'consensus', ['dhammika-prinsep', 'dhammika-edicts'], show=False),
 'c-greek-kings': c("One edict names five Greek kings, among them Antiochus II and Ptolemy II, to whom Ashoka sent envoys; their known dates anchor Mauryan chronology.", 'consensus', ['brit-ashoka-succ'], show=False),
 'c-dhamma': c("What Ashoka's dhamma meant is disputed.", 'debated', ['open-olivelle', 'dhammika-edicts'], "Some read it as Buddhist ethics with tolerance for all sects (S. Dhammika); Patrick Olivelle (2023) as an ecumenical 'civil religion' for a diverse empire; others as an ideology of control. Upinder Singh warns that a state programme of preaching and policing morality amounted to 'a form of authoritarianism'."),
 'c-maurya-end': c("In about 185 BCE the general Pushyamitra killed the last Mauryan king and founded the Shunga dynasty.", 'approx', ['brit-ashoka-succ', 'brit-shunga'], "The date is approximate."),
 'c-pushyamitra': c("Later Buddhist tradition says Pushyamitra persecuted Buddhists, but the accounts are late and Buddhism still flourished in his lands.", 'tradition', ['brit-shunga'], "No contemporary evidence supports a persecution."),
 'c-maurya-decline': c("Why the Mauryan empire fell so soon after Ashoka is debated.", 'debated', ['pwc-mauryan-decline'], "Explanations include a Brahmin reaction (H. P. Shastri), the weakening effect of Ashoka's pacifism (H. C. Raychaudhuri), fiscal strain (D. D. Kosambi), over-centralisation (Romila Thapar) and the rise of regional powers (R. S. Sharma)."),
 'c-bahaj': c("In 2025 an Archaeological Survey of India paper claimed Brahmi letters on sealings from Bahaj in Rajasthan dated by their layer to about 600 BCE, long before Ashoka.", 'debated', ['print-bahaj2025', 'coningham1996', 'knaw-schmid'], "New and unconfirmed: the date rests on the layer, with no radiocarbon dates or independent review yet. Inscribed sherds from Anuradhapura in Sri Lanka, dated to the early 4th century BCE, already show Brahmi in use somewhat before Ashoka; Charlotte Schmid (2024) asks whether Ashoka invented a script or put an existing one to new use."),
}

# ---------------------------------------------------------------- 9.4
P4 = {
 'title': "The Han economy", 'sub': "salt, iron, coins and paper",
 'lede': "In 81 BCE the Han court staged a debate over whether the state should run the salt and iron industries. The written record of it is one of the oldest surviving arguments about state ownership versus private enterprise, and the economist and the politician in you will recognise both sides.",
 'body': [
  "Emperor Wu's wars against the Xiongnu (see 9.5) were ruinously expensive. To pay for them, his ministers made salt, iron and liquor state monopolies and set up state trading offices to buy cheap and sell dear. [[c-iron-monopoly]] They also replaced the coinage with the wuzhu, minted only by the state, which lasted in some form for seven centuries. [[c-wuzhu]]",
  "After Wu's death the court called a debate. [[c-saltiron-debate]] The Confucian literati argued that a government seeking profit corrupts its people; [[c-literati-case]] the minister Sang Hongyang answered that the frontier had to be paid for and that state trading kept prices steady. [[c-sang-case]] Critics added that state iron tools were poor and dear. [[c-iron-critics]] The record we have was compiled later and is a literary reconstruction, not a transcript. [[c-yantielun]] The officials largely won, but the monopolies came and went for another century, [[c-monopoly-swings]] and archaeology suggests they never reached everywhere. [[c-monopoly-reach]]",
  "Most people were farmers who paid a light land tax and a heavy load of labour and military service. [[c-han-tax]] The census of 2 CE counted almost 60 million registered people. [[c-census2]] Over time, land concentrated in the hands of great families, who controlled local government and hid their tenants from the tax registers. [[c-great-families]] Wang Mang, who usurped the throne in 9 CE, tried to stop this by nationalising land; his reforms collapsed, and so did he. [[c-wangmang]]",
  "The Han also gave the world paper. Tradition credits the court official Cai Lun in 105 CE, [[c-cailun]] but older paper has been dug up in the north-west, including a fragment with a map on it whose status is still argued over. [[c-fangmatan]]",
  {'table': {'head': ["Year", "The state and industry"], 'rows': [
    ["118 BCE", "wuzhu coin introduced"],
    ["c. 119-110 BCE", "salt and iron monopolies set up"],
    ["81 BCE", "the Debate on Salt and Iron"],
    ["44-41 BCE", "monopolies abolished, then restored"],
    ["2 CE", "48 Iron Offices; census of 59.6 million"],
    ["9-23 CE", "Wang Mang's land and coin reforms fail"],
    ["85-88 CE", "monopolies revived, then dropped"]], 'note': "[[c-wuzhu]] [[c-iron-monopoly]] [[c-saltiron-debate]] [[c-monopoly-swings]] [[c-census2]] [[c-wangmang]]"}}],
 'figure': {'kind': 'chart', 'chart': 'ledger', 'signs': False, 'caption': "The Debate on Salt and Iron, 81 BCE", 'title': "Should the state run the salt and iron industries?",
  'left': {'h': 'The officials (Sang Hongyang)', 'items': [
   {'t': 'The frontier against the Xiongnu must be paid for', 's': 'Yantie lun'},
   {'t': 'State trading keeps prices steady', 's': "the 'equable marketing' system"},
   {'t': "'Abolition of these measures is not expedient!'", 's': 'Sang Hongyang'},
   {'t': 'Large state works can make iron at scale', 's': '48 Iron Offices by 2 CE (Wagner)'}]},
  'right': {'h': 'The Confucian literati', 'items': [
   {'t': 'Government must never be run for profit', 's': 'the literati'},
   {'t': 'Monopolies teach people to chase profit, not to farm', 's': 'Yantie lun'},
   {'t': "State tools are 'crude and coarse', and dear", 's': 'critics quoted by Wagner'},
   {'t': 'Virtue, not force, wins over distant peoples', 's': 'the Confucian position'}]},
  'notes': ["The record was compiled later by Huan Kuan; it is a literary work, not a transcript."]},
 'practice': [
  q("In the debate of 81 BCE, what was Sang Hongyang's main defence of the monopolies?",
    ["They paid for the Xiongnu frontier and kept prices steady", "The Confucian classics required the state to own industry", "They protected the profits of the state paper industry", "They let the state abolish the land tax on farmers"], 0,
    "Sang Hongyang replied that the monopolies paid for defence against the Xiongnu and that state trading kept prices steady.",
    {1: "It was the literati who appealed to Confucian morality, and they argued against a government seeking profit.", 2: "The monopolies covered salt, iron and liquor; Cai Lun's paper is dated 105 CE.", 3: "The land tax continued, at one-thirtieth or sometimes one-fifteenth of the harvest."}),
  q("What does the Fangmatan fragment suggest about Cai Lun's 'invention' of paper in 105 CE?",
    ["Paper may be older, though some doubt this is true paper", "It proves his exact paper method was used 250 years earlier", "It shows he was a legend, as the Han history omits him", "It suggests his own workshop stood in Gansu, where it lay"], 0,
    "The fragment is dated to the Western Han, perhaps 250 years before Cai Lun; Li Xiaocen accepts it as paper made by a different process, while Chen Gang says it needs more study.",
    {1: "Li Xiaocen, who accepts it as paper, says it was made by a different process.", 2: "The Han history records Cai Lun as a court official who presented a paper-making method.", 3: "It is dated perhaps 250 years before Cai Lun, so it cannot come from his workshop."})]}

# ---------------------------------------------------------------- 9.5
P5 = {
 'title': "Han and the steppe", 'sub': "the Xiongnu, Zhang Qian and the road west",
 'lede': "China's greatest security problem for two thousand years was the steppe to its north. The Han first paid the nomad Xiongnu to stay away, then fought them for decades, and in doing so pushed Chinese power and Chinese envoys deep into Central Asia.",
 'body': [
  "The Xiongnu were a confederation of mounted herders who became a great power under Maodun at the same moment the Han was founded. [[c-maodun]] For seventy years the Han emperors bought peace with silk, gold and brides. [[c-heqin]] Ancient DNA shows the Xiongnu empire was itself a mosaic of peoples. [[c-xiongnu-dna]]",
  "Emperor Wu reversed the policy. From 133 BCE he sent huge armies onto the steppe; they drove the Xiongnu back but emptied the treasury, which is why his ministers turned to monopolies (see 9.4). [[c-wu-wars]] Looking for allies, he sent Zhang Qian west to find the Yuezhi; Zhang was captured, escaped, and came home thirteen years later with the first Chinese reports of Ferghana, Bactria and lands beyond. [[c-zhangqian]] Han armies later marched as far as Ferghana for its horses. [[c-ferghana]] The Xiongnu eventually split, and the eastern half submitted. [[c-xiongnu-split]]",
  "To hold the road west, the Han built walls and beacon towers through the Hexi corridor to Dunhuang. [[c-hexi-wall]] At the relay station of Xuanquanzhi, archaeologists found tens of thousands of objects, [[c-xuanquan]] including wooden slips that log the envoys, foreign delegations and officials who passed through. [[c-xuanquan-slips]] This network is what UNESCO now lists as the Silk Roads. [[c-silkroads-unesco]]",
  "The name itself is modern, [[c-silkroad-term]] and historians disagree about how much trade the routes actually carried. [[c-silkroad-trade]] What the slips show most clearly is the state: soldiers, envoys and officials moving on government business, fed and housed at public expense.",
  {'table': {'head': ["Year (BCE)", "Han and the Xiongnu"], 'rows': [
    ["c. 209", "Maodun leads the Xiongnu"],
    ["to c. 135", "heqin: peace bought with silk and marriages"],
    ["138", "Zhang Qian sets out for the Yuezhi"],
    ["133", "Emperor Wu goes on the attack"],
    ["from 121", "walls through the Hexi corridor"],
    ["104 and 101", "campaigns to Ferghana"],
    ["65", "envoy Chang Hui logged at Xuanquanzhi"],
    ["51", "the Xiongnu split; the eastern half submits"]], 'note': "[[c-maodun]] [[c-heqin]] [[c-zhangqian]] [[c-wu-wars]] [[c-hexi-wall]] [[c-ferghana]] [[c-xuanquan-slips]] [[c-xiongnu-split]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 88.0, 'lat': 39.0, 'zoom': 6.3}, 'caption': "Han and the steppe, 2nd-1st centuries BCE", 'hint': "Click a place",
  'legend': [['acc dash', "Zhang Qian's journey, 138-126 BCE (simplified)"], ['dash', 'Han walls, from 121 BCE'], ['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'route', 'items': [{'path': [[108.93, 34.26], [103.8, 36.1], [102.63, 37.93], [98.52, 39.74], [94.68, 40.17], [89.19, 42.95], [82.96, 41.72], [75.99, 39.47], [72.8, 40.53], [70.94, 40.53], [66.97, 39.65], [66.9, 36.76]], 'label': 'Zhang Qian', 'lab': [82.96, 41.72], 'ldy': -12, 'acc': True, 'head': True}]},
   {'type': 'route', 'items': [{'path': [[103.8, 36.1], [102.63, 37.93], [100.45, 38.93], [98.52, 39.74], [95.4, 40.3], [94.68, 40.17], [93.86, 40.35]], 'label': 'Hexi walls', 'lab': [101.5, 38.4], 'ldy': 24}]},
   {'type': 'region', 'items': [{'ll': [97.0, 45.0], 'label': 'XIONGNU', 'size': 13}, {'ll': [110.5, 31.0], 'label': 'HAN CHINA', 'size': 12}, {'ll': [83.0, 39.0], 'label': 'TARIM BASIN', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [108.929, 34.258], 'label': "Chang'an", 'date': 'Han capital', 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '9.5 · the court', 'title': "Emperor Wu's wars", 'sub': '141-87 BCE', 'text': "[[c-heqin]] [[c-wu-wars]] [[c-zhangqian]]", 'sources': ['brit-wudi', 'brit-han', 'brit-zhangqian']}},
            {'ll': [94.683, 40.167], 'label': 'Dunhuang', 'acc': True, 'big': True, 'dy': -10, 'plate': {'kicker': '9.5 · the frontier', 'title': 'Dunhuang', 'sub': 'reached by the walls c. 100 BCE', 'text': "[[c-hexi-wall]] [[c-silkroads-unesco]]", 'sources': ['brit-greatwall-han', 'unesco-silkroads']}},
    {'ll': [95.4, 40.3], 'label': 'Xuanquanzhi', 'date': 'relay station', 'acc': True, 'dy': 18, 'plate': {'kicker': '9.5 · the slips', 'title': 'Xuanquanzhi', 'sub': '2nd century BCE to 2nd century CE', 'text': "[[c-xuanquan]] [[c-xuanquan-slips]] [[c-silkroad-trade]]", 'sources': ['cd-xuanquan2023', 'cd-xuanquan2025', 'whitfield-tarim']}},
        {'ll': [70.94, 40.53], 'label': 'Ferghana', 'date': 'horses, 101 BCE', 'acc': True, 'dy': 16, 'plate': {'kicker': '9.5 · Ferghana', 'title': 'The heavenly horses', 'sub': '104 and 101 BCE', 'text': "[[c-ferghana]]", 'sources': ['brit-wudi']}},
    {'ll': [66.897, 36.756], 'label': 'Bactra', 'date': 'Zhang Qian meets the Yuezhi', 'acc': True, 'dy': 16, 'plate': {'kicker': '9.5 · Zhang Qian', 'title': 'Zhang Qian', 'sub': '138 to c. 126 BCE', 'text': "[[c-zhangqian]]", 'sources': ['brit-zhangqian', 'benjamin2018']}},
    {'ll': [104.0, 47.0], 'label': 'Mongolian steppe', 'date': 'Xiongnu cemeteries', 'plate': {'kicker': '9.5 · the Xiongnu', 'title': 'The Xiongnu', 'sub': 'a multiethnic empire', 'text': "[[c-maodun]] [[c-xiongnu-dna]] [[c-xiongnu-split]]", 'sources': ['brit-maodun', 'sd-xiongnu2023', 'brit-xiongnu']}}]}]},
 'practice': [
  q("Why did Emperor Wu send Zhang Qian west in 138 BCE?",
    ["To win the Yuezhi as allies against the Xiongnu", "To buy Ferghana's 'blood-sweating' horses for the army", "To open a route west for Chinese silk merchants", "To arrange a heqin marriage with the Xiongnu ruler"], 0,
    "Zhang Qian went to find the Yuezhi, enemies of the Xiongnu; the mission was part of the war against them.",
    {1: "The horses came later, when Han armies marched to Ferghana in 104 and 101 BCE.", 2: "The mission sought allies against the Xiongnu; the name 'Silk Road' is a 19th-century German coinage.", 3: "He went to find the Xiongnu's enemies, and the Xiongnu held him captive for about ten years."}),
  q("Which statement best captures the Hansen-Whitfield debate about the Silk Road?",
    ["Both accept low volume; Whitfield says high-value trade mattered", "Both accept low volume; Hansen says the luxury trade mattered", "Hansen sees vast private caravans; Whitfield sees mostly state supply", "Whitfield finds a large volume; Hansen finds mostly local trade"], 0,
    "They agree on volume and disagree on significance: Hansen thinks the trade was small and mostly local and credits state spending on garrisons; Whitfield accepts the low volume but argues that high-value long-distance trade mattered.",
    {1: "That is Whitfield's position; Hansen argues that prosperity in the north-west came from state spending on garrisons.", 2: "Hansen argues the volume was small and mostly local, with prosperity coming from state spending.", 3: "Whitfield accepts the low volume; her point is that high-value long-distance trade still mattered."})]}

# ---------------------------------------------------------------- 9.6
P6 = {
 'title': "Magadha to the Mauryas", 'sub': "India's first empire, c. 321-185 BCE",
 'lede': "A few years after Alexander's army turned back at the Beas, a young adventurer named Chandragupta seized the throne of Magadha and built an empire across most of the subcontinent. We see it through a lost Greek travel book, a treatise on statecraft of uncertain date, and the ruins under modern Patna.",
 'body': [
  "Magadha, on the middle Ganges, had been the strongest kingdom of the Buddha's day (see 7.9). Under the Nanda kings it grew rich on land revenue. [[c-nandas]] About 321 BCE Chandragupta Maurya overthrew them and went on to build the first empire to span most of India. [[c-chandragupta]] When Alexander's successor Seleucus tried to recover the Indus lands, the two kings fought and then made a treaty: Seleucus gave up the territory in return for 500 elephants. [[c-seleucus]]",
  "Seleucus sent an ambassador, Megasthenes, whose book on India survives only in quotations. [[c-megasthenes]] He describes Pataliputra as a vast walled city with 570 towers, [[c-pataliputra-arrian]] run by boards of officials. [[c-pataliputra-gov]] Excavations in Patna have found part of a great hall of polished stone pillars, now being uncovered again. [[c-kumrahar]] [[c-kumrahar-council]]",
  "The other famous source is the Arthashastra, a manual on how a king should run a state: tax, trade, spies, law and war. Tradition makes its author Chandragupta's minister Kautilya, [[c-kautilya]] but scholars now think it was written by several hands and reworked over centuries. [[c-arthashastra-date]] [[c-arthashastra-authors]] It is still one of the most hard-headed books on government ever written, and is often compared with Machiavelli.",
  {'table': {'head': ["Source", "Date", "What it gives us", "Caution"], 'rows': [
    ["Megasthenes, Indica", "c. 300 BCE", "an outsider's view of the court and capital", "lost; known only from later quotations"],
    ["Arthashastra", "core perhaps Mauryan; text later", "theory of the state, tax and trade", "several authors; reworked"],
    ["Ashoka's edicts", "c. 260-230 BCE", "the king's own words (see 9.7)", "royal self-presentation"],
    ["Kumrahar excavations", "Mauryan levels", "the capital's buildings", "much lies under modern Patna"]], 'note': "[[c-megasthenes]] [[c-arthashastra-date]] [[c-kumrahar]]"}}],
 'figure': {'kind': 'chart', 'chart': 'ranges', 'caption': "The Mauryas and their sources", 'title': "Rulers, a lost book and a treatise of uncertain date",
  'max': 360, 'min': -320, 'unit': 'ka', 'ticks': [300, 200, 100, 0, -100, -200, -300], 'tickLabels': ['300 BCE', '200', '100 BCE', '1 CE', '100 CE', '200', '300 CE'],
  'axis': "years BCE and CE; all dates approximate", 'hint': "Hover or click a row",
  'marks': [{'ya': 326, 't': 'Alexander at the Beas, 326'}, {'ya': 305, 't': 'Seleucus cedes the Indus lands, c. 305'}],
  'rows': [
   {'t': 'Chandragupta', 'sub': 'founder', 'from': 321, 'to': 297, 'lab': 'c. 321-297', 'acc': True, 'plate': {'kicker': '9.6 · the Mauryas', 'title': 'Chandragupta Maurya', 'sub': 'c. 321 to 297 BCE', 'text': "[[c-nandas]] [[c-chandragupta]] [[c-seleucus]]", 'sources': ['brit-magadha']}},
   {'t': 'Bindusara', 'from': 297, 'to': 272, 'lab': 'c. 297-272', 'acc': True},
   {'t': 'Ashoka', 'from': 268, 'to': 232, 'lab': 'c. 268-232', 'acc': True, 'plate': {'kicker': '9.7 · Ashoka', 'title': 'Ashoka', 'sub': 'c. 268 to 232 BCE', 'text': "[[c-ashoka-dates]] [[c-re13]]", 'sources': ['brit-ashoka-succ', 'dhammika-edicts']}},
   {'t': 'Mauryan empire', 'from': 321, 'to': 185, 'lab': 'c. 321-185', 'plate': {'kicker': '9.7 · the end', 'title': 'The end of the Mauryas', 'sub': 'c. 185 BCE', 'text': "[[c-maurya-end]] [[c-maurya-decline]]", 'sources': ['brit-shunga', 'pwc-mauryan-decline']}},
   {'t': 'Megasthenes', 'sub': 'envoy; Indica lost', 'from': 350, 'to': 290, 'lab': 'c. 350-290', 'open': True, 'plate': {'kicker': '9.6 · Megasthenes', 'title': 'Megasthenes', 'sub': 'Indica', 'text': "[[c-megasthenes]] [[c-pataliputra-arrian]]", 'sources': ['brit-megasthenes', 'arrian-indica10']}},
   {'t': 'Arthashastra', 'sub': 'range of proposed dates', 'from': 350, 'to': -300, 'lab': '', 'open': True, 'plate': {'kicker': '9.6 · the Arthashastra', 'title': 'The Arthashastra', 'sub': '4th century BCE to 3rd century CE', 'text': "[[c-kautilya]] [[c-arthashastra-date]] [[c-arthashastra-authors]]", 'sources': ['brit-magadha', 'trautmann1968', 'mcclish2019']}}]},
 'practice': [
  q("Why are historians cautious about reading the Arthashastra as a handbook of Chandragupta's actual government?",
    ["It had several authors and was reworked after Mauryan times", "It survives in a Greek version quoted by Megasthenes", "Its author is named as Ashoka's minister, not Chandragupta's", "Olivelle dates the whole text to the 4th century BCE"], 0,
    "Statistical study of its vocabulary suggests different authors and later reworking, and Patrick Olivelle dates the surviving text to the first centuries CE, so its Mauryan core reaches us in a later, layered form.",
    {1: "It is a Sanskrit treatise; Megasthenes wrote his own book, the Indica, which is lost.", 2: "Tradition names Kautilya, Chandragupta's chief minister, as its author.", 3: "Olivelle dates the surviving work to the first centuries CE."}),
  q("How should a historian use Megasthenes' figure of 570 towers at Pataliputra?",
    ["As a lost eyewitness's figure, known only through Arrian", "As an exact count copied from his surviving original", "As a report by Alexander's own envoy to Chandragupta", "As a figure confirmed by the towers excavated at Kumrahar"], 0,
    "The Indica is lost; the figure reaches us through Arrian's quotation and cannot be checked.",
    {1: "The Indica is lost and known only through later writers.", 2: "Megasthenes was the envoy of Seleucus I, Alexander's successor.", 3: "Kumrahar yielded a hall of 80 stone pillars, not towers; Megasthenes' figures cannot be checked."})]}

# ---------------------------------------------------------------- 9.7
P7 = {
 'title': "Ashoka", 'sub': "the emperor who said sorry, c. 268-232 BCE",
 'lede': "Ashoka conquered Kalinga, an independent kingdom on India's east coast, counted the dead, and then had his regret carved into rock across his empire. His inscriptions are the first long texts from India that can be read, and the first time an Indian ruler speaks to us in his own words.",
 'body': [
  "Chandragupta's grandson Ashoka attacked Kalinga about eight years after he took the throne. [[c-ashoka-dates]] In Rock Edict 13 he gives the toll in his own words and says he now prefers 'conquest by Dhamma'. [[c-re13]] That edict, however, was left out of the inscriptions set up in Kalinga itself. [[c-re13-absent]]",
  "The edicts were carved on rocks at the edges of the empire and on polished pillars along its roads, at more than thirty sites. [[c-edict-sites]] They speak in the local language and script: Prakrit in Brahmi across most of India, Kharosthi in the north-west, and Greek and Aramaic near Kandahar, where Greek settlers lived. [[c-edict-scripts]] [[c-kandahar-edict]] One edict names the Greek kings to whom Ashoka sent envoys, which lets historians date his reign. [[c-greek-kings]] Ashoka's form of the script was forgotten for well over a thousand years until James Prinsep deciphered it in 1837. [[c-prinsep]] A 2025 claim of much earlier Brahmi remains unconfirmed. [[c-bahaj]]",
  "What did Ashoka want? The edicts urge respect for parents, kindness to animals, tolerance of all sects and honest officials, enforced by special 'dhamma ministers'. Ashoka was a Buddhist, but scholars disagree about whether his dhamma was Buddhism, a civic morality for a diverse empire, or a tool of control. [[c-dhamma]]",
  "Within fifty years of his death the empire was gone. A general killed the last Maurya in about 185 BCE, [[c-maurya-end]] and later Buddhist writers made him a persecutor. [[c-pushyamitra]] Why the empire collapsed so fast is one of the classic debates of Indian history. [[c-maurya-decline]]",
  {'table': {'head': ["Where", "Language and script", "Example"], 'rows': [
    ["most of India", "Prakrit in Brahmi", "Girnar, Kalsi, Dhauli, Delhi-Topra pillar"],
    ["north-west (Pakistan)", "Prakrit in Kharosthi", "Shahbazgarhi, Mansehra"],
    ["Kandahar (Afghanistan)", "Greek and Aramaic", "bilingual edict, found 1958"],
    ["Lumbini (Nepal)", "Prakrit in Brahmi", "pillar marking the Buddha's birthplace"]], 'note': "[[c-edict-scripts]] [[c-kandahar-edict]] [[c-edict-sites]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 77.5, 'lat': 25.0, 'zoom': 11}, 'caption': "Ashoka's edicts, c. 260-230 BCE", 'hint': "Click a place",
  'legend': [['dot', 'edict in Brahmi script'], ['pt', 'edict in Kharosthi, Greek or Aramaic; or the capital'], ['zone', 'Kalinga']], 'seas': False,
  'layers': [
   {'type': 'zone', 'items': [{'ll': [85.0, 20.0], 'r': 1.6, 'label': 'KALINGA', 'lab': [86.8, 17.4]}]},
   {'type': 'region', 'items': [{'ll': [85.6, 24.6], 'label': 'MAGADHA', 'size': 10}, {'ll': [70.5, 29.0], 'label': 'INDUS', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [85.189, 25.598], 'label': 'Pataliputra', 'date': 'capital', 'big': True, 'dy': -10, 'plate': {'kicker': '9.6 · the capital', 'title': 'Pataliputra', 'sub': 'modern Patna', 'text': "[[c-pataliputra-arrian]] [[c-pataliputra-gov]] [[c-kumrahar]]", 'sources': ['arrian-indica10', 'brit-magadha', 'organiser-kumrahar']}},
    {'ll': [85.833, 20.183], 'label': 'Dhauli', 'date': 'no Edict 13', 'acc': True, 'big': True, 'dy': -8, 'plate': {'kicker': '9.7 · Kalinga', 'title': 'The Kalinga war', 'sub': 'c. 260 BCE', 'text': "[[c-re13]] [[c-re13-absent]]", 'sources': ['dhammika-edicts']}},
    {'ll': [84.831, 19.523], 'label': 'Jaugada', 'acc': True, 'anchor': 'end', 'dy': 14},
    {'ll': [70.55, 21.5], 'label': 'Girnar', 'acc': True, 'anchor': 'end'},
    {'ll': [77.847, 30.538], 'label': 'Kalsi', 'acc': True, 'dy': -8},
    {'ll': [77.244, 28.636], 'label': 'Delhi-Topra pillar', 'date': 'read by Prinsep, 1837', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '9.7 · decipherment', 'title': 'James Prinsep', 'sub': '1837', 'text': "[[c-prinsep]] [[c-bahaj]]", 'sources': ['dhammika-prinsep', 'print-bahaj2025']}},
    {'ll': [83.025, 25.381], 'label': 'Sarnath', 'acc': True, 'anchor': 'end', 'dy': 14},
    {'ll': [83.277, 27.486], 'label': 'Lumbini', 'acc': True, 'dy': -8},
    {'ll': [72.15, 34.2], 'label': 'Shahbazgarhi', 'date': 'Kharosthi', 'anchor': 'end', 'dy': 14},
    {'ll': [73.197, 34.33], 'label': 'Mansehra', 'dy': -8},
    {'ll': [65.717, 31.617], 'label': 'Kandahar', 'date': 'Greek and Aramaic', 'dy': 16, 'plate': {'kicker': '9.7 · the north-west', 'title': 'The Kandahar edict', 'sub': 'Greek and Aramaic', 'text': "[[c-kandahar-edict]] [[c-greek-kings]] [[c-edict-scripts]]", 'sources': ['lhi-kandahar', 'brit-ashoka-succ', 'unesco-shahbazgarhi']}}]}]},
 'practice': [
  q("What is Rock Edict 13 best evidence for?",
    ["Ashoka's own account of the war and his turn to dhamma", "Chandragupta's conquest of Kalinga in about 305 BCE", "The version carved at Dhauli and Jaugada, in Kalinga itself", "Ashoka's decree making Buddhism the state religion"], 0,
    "It is Ashoka's own retrospective account of the Kalinga war and of his turn to 'conquest by Dhamma': royal self-presentation, whose figures cannot be checked.",
    {1: "The edict says Ashoka himself attacked Kalinga, about eight years after he took the throne.", 2: "At Dhauli and Jaugada, in Kalinga itself, Rock Edicts 11-13 were left out and Separate Edicts carved instead.", 3: "The edicts urge tolerance of all sects, and scholars disagree whether his dhamma was Buddhism at all."}),
  q("Which statement about the end of the Maurya dynasty is best supported?",
    ["General Pushyamitra killed the last king; causes are debated", "An Indo-Greek king killed the last Maurya; causes are debated", "Romila Thapar blamed Ashoka's pacifism for the collapse", "Contemporary inscriptions show Pushyamitra persecuted Buddhists"], 0,
    "In about 185 BCE the general Pushyamitra killed the last Mauryan king and founded the Shunga dynasty; why the empire fell so soon after Ashoka is still argued over.",
    {1: "It was the general Pushyamitra, who founded the Shunga dynasty.", 2: "That was H. C. Raychaudhuri's view; Thapar stressed over-centralisation.", 3: "The persecution story comes from late Buddhist tradition; no contemporary evidence supports it, and Buddhism still flourished in his lands."})]}

PAGES = [P4, P5, P6, P7]
