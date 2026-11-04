# Chapter 12, pages 12.4 to 12.7. Coordinates are [longitude, latitude].
from common import c, q

S = {
 # 12.4
 'je-blackdeath': ("Jewish Encyclopedia (1906), \"Black Death\"", "https://jewishencyclopedia.com/articles/3349-black-death"),
 'fordham-konigshofen': ("Jacob von Königshofen, chronicle of Strasbourg, tr. Jacob Marcus (1938), Fordham Jewish History Sourcebook", "https://sourcebooks.web.fordham.edu/jewish/1348-jewsblackdeath.asp"),
 'jvl-bulls': ("Jewish Virtual Library, \"Papal bulls\"", "https://www.jewishvirtuallibrary.org/papal-bulls"),
 'jjk-persecution': ("Jedwab, Johnson and Koyama, \"Negative shocks and mass persecutions: evidence from the Black Death\", George Washington University IIEP", "https://iiep.gwu.edu/negative-shocks-and-mass-persecutions-evidence-black-death"),
 'fitz-flagellants': ("Fitzwilliam Museum, Cambridge, \"The flagellants\"", "https://fitzmuseum.cam.ac.uk/objects-and-artworks/highlights/context/stories-and-histories/the-flagellants"),
 'fordham-ordinance': ("Ordinance of Labourers (1349), ed. White and Notestein (1915), Fordham Internet History Sourcebooks", "https://sourcebooks.web.fordham.edu/seth/ordinance-labourers.asp"),
 'avalon-labourers': ("The Ordinance of Labourers (1349), printed as \"The Statute of Laborers; 1351\", Avalon Project, Yale Law School", "https://avalon.law.yale.edu/medieval/statlab.asp"),
 'brit-peasants': ("Encyclopaedia Britannica, \"Peasants' Revolt\"", "https://www.britannica.com/event/Peasants-Revolt"),
 'teams-ball': ("TEAMS Middle English Texts, University of Rochester: John Ball's couplet", "https://d.lib.rochester.edu/node/33490"),
 'munro-serfdom': ("John Munro, University of Toronto, lecture notes on serfdom in medieval and early modern Europe", "https://www.economics.utoronto.ca/munro5/07agrmd1.pdf"),
 'pamuk2007': ("Şevket Pamuk, \"The Black Death and the origins of the 'Great Divergence' across Europe, 1300-1600\", European Review of Economic History 11 (2007)", "https://econpapers.repec.org/RePEc:cup:ereveh:v:11:y:2007:i:03:p:289-317_00"),
 'vv2013': ("Voigtländer and Voth, \"The three horsemen of riches\", Review of Economic Studies (2013)", "https://www.jvoth.com/papers/three-horsemen-of-riches.html"),
 'jjk2022': ("Jedwab, Johnson and Koyama, \"The economic impact of the Black Death\", Journal of Economic Literature 60 (2022)", "https://www.aeaweb.org/doi/10.1257/jel.20201639"),
 'alfani2022': ("Guido Alfani, \"Epidemics, inequality, and poverty in preindustrial and early industrial times\", Journal of Economic Literature 60 (2022)", "https://www.aeaweb.org/doi/10.1257/jel.20201640"),
 'mcmaster-immune': ("McMaster Ancient DNA Centre, \"Evolution of immune genes is associated with the Black Death\" (2022)", "https://sexuality.mcmaster.ca/mcmaster-ancient-dna-centre/news/evolution-of-immune-genes-is-associated-with-the-black-death"),
 # 12.5
 'brit-hyw': ("Encyclopaedia Britannica, \"Hundred Years' War\" (summary)", "https://www.britannica.com/summary/Hundred-Years-War"),
 'brit-joan': ("Encyclopaedia Britannica, \"Saint Joan of Arc\" (summary)", "https://www.britannica.com/summary/Saint-Joan-of-Arc"),
 'brit-schism': ("Encyclopaedia Britannica, \"Western Schism\"", "https://www.britannica.com/event/Western-Schism"),
 'brit-lollards': ("Encyclopaedia Britannica, \"Lollard\"", "https://www.britannica.com/topic/Lollards"),
 'ht-wycliffe': ("History Today, \"John Wycliffe condemned as a heretic\"", "https://www.historytoday.com/archive/john-wycliffe-condemned-heretic"),
 'brit-hus': ("Encyclopaedia Britannica, \"Jan Hus: the final trial\"", "https://www.britannica.com/biography/Jan-Hus/The-final-trial"),
 'uw-petrarch': ("University of Washington, HSTEU 401 lecture, \"Petrarch and humanism\"", "https://courses.washington.edu/hsteu401/Petrarch%20Humanism%20lecture.htm"),
 'brit-giovanni': ("Encyclopaedia Britannica, \"Giovanni di Bicci de' Medici\"", "https://www.britannica.com/biography/Giovanni-di-Bicci"),
 'loc-gutenberg': ("Library of Congress, \"The Gutenberg Bible\"", "https://www.loc.gov/exhibits/bibles/interactives/gutenberg/index.html"),
 # 12.6
 'loc-partidas': ("Library of Congress (World Digital Library), Las Siete Partidas", "https://www.loc.gov/item/2021667865/"),
 'fancy2014': ("Hussein Fancy, review of Paola Tartakoff, Studies in Christian-Jewish Relations 9 (2014)", "https://ejournals.bc.edu/index.php/scjr/article/download/5792/5164/11557"),
 'brit-inq-timeline': ("Encyclopaedia Britannica, \"Timeline of the Spanish Inquisition\"", "https://www.britannica.com/list/timeline-of-the-spanish-inquisition"),
 'jvl-tortosa': ("Jewish Virtual Library (Encyclopaedia Judaica), \"Tortosa, Disputation of\"", "https://www.jewishvirtuallibrary.org/tortosa-disputation-of"),
 'brit-isabella': ("Encyclopaedia Britannica, \"Isabella I\" (summary)", "https://www.britannica.com/summary/Isabella-I-queen-of-Spain"),
 'brit-muhammad12': ("Encyclopaedia Britannica, \"Muhammad XII\"", "https://www.britannica.com/biography/Muhammad-XII"),
 'cojs-alhambra': ("Edict of the Expulsion of the Jews (1492), tr. Edward Peters, Center for Online Judaic Studies", "https://cojs.org/Edict_of_the_Expulsion_of_the_Jews_from_Spain-_1492/"),
 'lemans-expulsion': ("Université du Mans, HEMED course, \"The expulsion of 1492\"", "https://hemed.univ-lemans.fr/cours2010/en/co/1-1-2.html"),
 'enc-starrlebeau': ("Gretchen Starr-LeBeau, \"Jews, expulsion of (Spain; Portugal)\", Europe 1450 to 1789, via Encyclopedia.com", "https://www.encyclopedia.com/history/encyclopedias-almanacs-transcripts-and-maps/jews-expulsion-spain-portugal"),
 'loc-alhambra-blog': ("Library of Congress, In Custodia Legis, \"Alhambra Decree 521 years later\" (2013)", "https://blogs.loc.gov/law/2013/03/alhambra-decree-521-years-later/"),
 'local-sephardic': ("The Local Spain, \"72,000 foreigners with Sephardic Jewish ancestry granted Spanish citizenship\" (February 2025)", "https://www.thelocal.es/20250224/72000-foreigners-with-sephardic-jewish-ancestry-granted-spanish-citizenship"),
 'brit-henry': ("Encyclopaedia Britannica, \"Henry the Navigator\" (summary)", "https://britannica.com/summary/Henry-the-Navigator"),
 # 12.7
 'brit-timur': ("Encyclopaedia Britannica, \"Timur\" (summary)", "https://www.britannica.com/summary/Timur"),
 'unesco-samarkand': ("UNESCO World Heritage Centre, \"Samarkand - Crossroad of Cultures\"", "https://whc.unesco.org/en/list/603"),
 'brit-ankara': ("Encyclopaedia Britannica, \"Battle of Ankara\"", "https://www.britannica.com/event/Battle-of-Ankara"),
 'brit-osman-orhan': ("Encyclopaedia Britannica, \"Ottoman Empire: Osman and Orhan\"", "https://www.britannica.com/place/Ottoman-Empire/Osman-and-Orhan"),
 'ostour-gaza': ("Anis A. Mahmoud, on the gaza thesis and its critics, Ostour 9 (2019)", "https://ojs.acrps.ai/index.php/ostour/en/article/view/issue009-art04"),
 'brit-devsirme': ("Encyclopaedia Britannica, \"Devshirme\"", "https://britannica.com/topic/devsirme"),
 'brit-fall1453': ("Encyclopaedia Britannica, \"Fall of Constantinople\"", "https://www.britannica.com/event/Fall-of-Constantinople-1453"),
 'brit-mehmed': ("Encyclopaedia Britannica, \"Mehmed II: Mehmed's empire\"", "https://www.britannica.com/biography/Mehmed-II-Ottoman-sultan/Mehmeds-empire"),
 'sbs-hagiasophia': ("SBS News (2020), \"UNESCO 'deeply regrets' Turkey's conversion of Hagia Sophia into mosque\"", "https://www.sbs.com.au/news/unesco-deeply-regrets-turkey-s-conversion-of-hagia-sophia-into-mosque"),
}

C = {
 # 12.4
 'c-wells': c("As the plague spread, Christians accused Jews of plotting to destroy them by poisoning the wells, an accusation already made in Franconia in 1319.", 'consensus', ['je-blackdeath'], show=False),
 'c-strasbourg': c("In Strasbourg in February 1349 the Jews were burned on a wooden platform in their cemetery; the chronicler Jacob von Königshofen says about two thousand died, and that 'the money was indeed the thing that killed the Jews'.", 'approx', ['fordham-konigshofen', 'je-blackdeath'], "The number is the chronicler's. He dates it to St Valentine's Day (14 February); the Jewish Encyclopedia gives 16 February."),
 'c-clement': c("Pope Clement VI issued a bull in 1348 that urged the protection of Jews against the accusation that they had caused the plague by poisoning wells; Königshofen notes that in Avignon 'the pope protected them'.", 'consensus', ['jvl-bulls', 'fordham-konigshofen'], show=False),
 'c-jjk-persecution': c("An economic study of city-level data finds that persecution of Jews during the Black Death was less likely where Jews played important economic roles.", 'debated', ['jjk-persecution'], "A statistical inference by Jedwab, Johnson and Koyama; the Strasbourg chronicle, by contrast, points to debts and money as a motive."),
 'c-flagellants': c("Flagellants, who whipped themselves in public to share in Christ's sufferings, spread with the plague; Pope Clement VI condemned the practice in 1349.", 'consensus', ['fitz-flagellants'], show=False),
 'c-statute': c("England's Ordinance of Labourers (1349) complained that because 'a great part of the people' had died in the pestilence, workers would not serve 'unless they receive excessive wages', and tried to hold wages at pre-plague levels; the Statute of Labourers (1351) had the same aim.", 'consensus', ['fordham-ordinance', 'avalon-labourers', 'brit-peasants'], show=False),
 'c-peasants': c("The English Peasants' Revolt began in Essex in May 1381; the rebels resented the Statute of Labourers, and the young Richard II promised them the abolition of serfdom, a promise not kept.", 'consensus', ['brit-peasants'], show=False),
 'c-ball': c("The radical priest John Ball is remembered for the couplet 'Whan Adam dalf, and Eve span, / Wo was thanne a gentilman?', 'When Adam dug and Eve spun, who was then a nobleman?'", 'tradition', ['teams-ball'], "Attributed to Ball by the chronicler Thomas Walsingham; the modern English is ours, following the Rochester glosses. It uses the Genesis story of the first humans to question inherited rank."),
 'c-serfdom': c("By about 1500 serfdom had virtually disappeared in western Europe, while east of the Elbe a 'second serfdom', harsher than the first, spread from the 15th century.", 'debated', ['munro-serfdom'], "Why the two halves diverged is debated: Munro notes that population decline hastened serfdom's end in the West, while Robert Brenner attacked 'simplistic economic models of other historians that neglected to consider the dynamics of class relationships and class conflicts'."),
 'c-pamuk': c("Şevket Pamuk finds that after the plague real wages held up best in England and the Low Countries, so that a wage gap opened between north-west Europe and the rest of the continent after 1450.", 'debated', ['pamuk2007'], "One influential account of the roots of the 'Great Divergence'."),
 'c-vv': c("Nico Voigtländer and Joachim Voth argue that the Black Death raised wages sharply, and that plague, war and unhealthy cities then kept death rates and incomes high in Europe.", 'debated', ['vv2013'], "Their 'three horsemen of riches' model (2013)."),
 'c-jjk-survey': c("A 2022 survey concludes that the plague raised wages, but that 'in the long run, this rise was only sustained in some parts of Europe'.", 'debated', ['jjk2022'], "Jedwab, Johnson and Koyama link the plague to the end of western serfdom and to the beginnings of Europe's divergence from other regions."),
 'c-alfani': c("Guido Alfani notes that the Black Death 'is usually believed' to have reduced inequality, but that the record of other epidemics makes the picture 'much more complex'.", 'debated', ['alfani2022'], "Alfani (2022)."),
 'c-immune': c("A 2022 ancient-DNA study suggests the plague favoured immune-gene variants that protected against it but that today are associated with a higher risk of autoimmune disease.", 'debated', ['mcmaster-immune'], "New and still being tested; based on 206 ancient samples from London, checked against Denmark."),
 # 12.5
 'c-hyw': c("The Hundred Years' War (1337-1453) was an intermittent conflict between England and France; despite English victories such as Crécy (1346) and Poitiers (1356), by 1453 England held only Calais.", 'consensus', ['brit-hyw'], show=False),
 'c-joan': c("Joan of Arc raised the siege of Orléans in 1429 and saw Charles VII crowned at Reims; tried for witchcraft and heresy, she was burned at Rouen on 30 May 1431, and was canonised in 1920.", 'consensus', ['brit-joan'], show=False),
 'c-joan-voices': c("Joan said she heard the voices of Saints Michael, Catherine and Margaret.", 'tradition', ['brit-joan'], "Her own testimony; believers and historians interpret it in different ways."),
 'c-schism': c("After almost 70 years in which the popes lived at Avignon, the Western Schism (1378-1417) produced two and then three rival popes, until the Council of Constance elected Martin V in November 1417.", 'consensus', ['brit-schism'], show=False),
 'c-wyclif': c("John Wyclif denied the doctrine of transubstantiation and stressed the primacy of Scripture; his followers, the Lollards, produced the first complete English Bible from 1382, and the Council of Constance condemned him in 1415.", 'consensus', ['brit-lollards', 'ht-wycliffe'], show=False),
 'c-hus': c("The Czech reformer Jan Hus came to Constance on King Sigismund's promise of safe-conduct, was arrested, tried as a follower of Wyclif and burned on 6 July 1415.", 'debated', ['brit-hus'], "The events are agreed; how far his ideas depended on Wyclif rather than on a Czech reform movement is debated."),
 'c-petrarch': c("Petrarch (1304-1374), crowned poet laureate in Rome in 1341, hunted for lost classical texts and found Cicero's letters to Atticus at Verona.", 'consensus', ['uw-petrarch'], show=False),
 'c-medici': c("Giovanni di Bicci de' Medici (1360-1429) founded the Medici bank and in 1422 became banker to the papacy; his son Cosimo dominated Florence from 1434.", 'consensus', ['brit-giovanni'], show=False),
 'c-gutenberg': c("The Gutenberg Bible (Mainz, c. 1455) was the first book printed with movable metal type in western Europe, about 180 copies; Korean printers had used movable metal type about a century earlier.", 'consensus', ['loc-gutenberg'], show=False),
 # 12.6
 'c-partidas': c("The Siete Partidas, a law code begun under Alfonso X of Castile (1221-1284), was recognised as a body of law at the Cortes of Alcalá de Henares in 1348 and influenced the law of some of Spain's former colonies.", 'consensus', ['loc-partidas'], show=False),
 'c-1391': c("In June 1391 Christian mobs attacked the Jews of Seville, killing thousands and forcing others into baptism; the violence spread across Castile, Aragon and Mallorca.", 'approx', ['fancy2014', 'brit-inq-timeline'], "The number killed is not known precisely. Those baptised and their descendants became known as conversos."),
 'c-1391-view': c("Historians once saw 1391 as the moment when 'centuries of coexistence gave way to expulsion and inquisition'.", 'debated', ['fancy2014'], "Recent work, such as Paola Tartakoff's, finds conflict over conversion earlier; compare the convivencia debate in 11.2."),
 'c-tortosa': c("At the Disputation of Tortosa (1413-14), called by the antipope Benedict XIII, the convert Gerónimo de Santa Fe argued from Jewish texts that the Messiah had come; it ran to 69 sessions and many conversions followed.", 'approx', ['jvl-tortosa'], "The Encyclopaedia Judaica calls it 'a propagandist missionary attack accompanied by psychological pressure'."),
 'c-isabella': c("Isabella of Castile married Ferdinand of Aragon in 1469 and became queen of Castile in 1474; from 1479 the two crowns were united in their persons.", 'consensus', ['brit-isabella'], show=False),
 'c-inquisition': c("In 1478 Pope Sixtus IV authorised the Spanish Inquisition, which held its first auto de fe in Seville in February 1481; under Tomás de Torquemada about 2,000 people were burned.", 'approx', ['brit-inq-timeline'], "The figure for Torquemada's time is Britannica's estimate."),
 'c-granada': c("Muhammad XII surrendered Granada to Ferdinand and Isabella on 2 January 1492, ending Muslim rule in Spain.", 'consensus', ['brit-muhammad12'], show=False),
 'c-alhambra': c("The Alhambra Decree of 31 March 1492 ordered the Jews of Ferdinand and Isabella's kingdoms to leave by the end of July, blaming the 'interaction between the Jews and these Christians', the conversos.", 'consensus', ['cojs-alhambra'], show=False),
 'c-expelled': c("How many Jews left Spain is debated: estimates run from 40,000-50,000 to 150,000-200,000.", 'debated', ['lemans-expulsion', 'enc-starrlebeau'], "Gretchen Starr-LeBeau, drawing on Henry Kamen, suggests 40,000-50,000 and notes that 'most converted rather than emigrated'; Luis Suárez gave 100,000; a French university course says most historians estimate 150,000-200,000."),
 'c-alhambra-memory': c("Spain declared the decree without effect in 1968, and under a 2015 law 72,199 people with Sephardic Jewish ancestry had been granted Spanish citizenship by the end of 2024.", 'consensus', ['loc-alhambra-blog', 'local-sephardic'], show=False),
 'c-henry': c("Prince Henry 'the Navigator' of Portugal (1394-1460) helped his father capture Ceuta in Morocco in 1415 and sponsored voyages to Madeira and down the coast of Africa.", 'consensus', ['brit-henry'], show=False),
 # 12.7
 'c-timur': c("Timur (1336-1405), a conqueror from Central Asia, massacred the populations of whole cities in Iran, invaded India in 1398 and died at Otrar at the start of a campaign against China.", 'consensus', ['brit-timur'], show=False),
 'c-samarkand': c("Samarkand was the capital of the Timurid realm, and Timur strove to make it the most splendid city in Asia; the city's main growth came in the Timurid period (14th-15th centuries), and its monuments include the Registan, the Bibi-Khanum mosque, the Gur-Emir mausoleum and Ulugh Beg's observatory.", 'consensus', ['unesco-samarkand', 'brit-timur'], show=False),
 'c-ankara': c("At Ankara on 20 July 1402 Timur defeated the Ottoman sultan Bayezid I, the only Ottoman ruler ever captured by an enemy; a civil war among his sons followed until 1413.", 'consensus', ['brit-ankara'], show=False),
 'c-osman': c("Osman emerged after 1293 as ruler of a small principality in north-western Anatolia; his son Orhan took Bursa in 1324 or 1326, and from 1354 Orhan's son Süleyman made Gallipoli a permanent base for expansion into Europe.", 'approx', ['brit-osman-orhan'], "Britannica notes that some sources date Bursa's fall to 1326."),
 'c-gaza': c("Why the Ottomans grew so fast is debated.", 'debated', ['ostour-gaza'], "Paul Wittek's thesis that they were driven by gaza, holy war against Christians, faced severe criticism from the 1980s that left it 'largely undermined' (Anis Mahmoud, 2019, whose bibliography includes Rudi Lindner, 1983, and Heath Lowry, 2003)."),
 'c-devsirme': c("Under the devshirme, Christian boys from the Balkan provinces were periodically conscripted and converted to Islam; the ablest were trained for government and the rest joined the Janissaries.", 'consensus', ['brit-devsirme'], show=False),
 'c-1453': c("Mehmed II took Constantinople on 29 May 1453 with perhaps 75,000-100,000 men against about 8,000 defenders; the last emperor, Constantine XI, died in the fighting, and Hagia Sophia was turned into a mosque.", 'approx', ['brit-fall1453'], "Troop numbers are estimates. Britannica notes that 1453 is widely quoted as the end of the European Middle Ages."),
 'c-mehmed': c("Mehmed II saw himself as heir both of the Roman Caesars and the champion of Islam, and had the Orthodox patriarch Gennadios write a statement of the Christian faith for him.", 'consensus', ['brit-mehmed'], show=False),
 'c-hagiasophia': c("In 2020 Turkey's highest administrative court cancelled the 1934 decision that had made Hagia Sophia a museum, and it reopened for Muslim worship.", 'debated', ['sbs-hagiasophia'], "Supporters said it would 'better reflect Turkey's status as an overwhelmingly Muslim country'; UNESCO said it 'deeply regrets the decision', and Greece called it an 'open provocation'."),
}

# ---------------------------------------------------------------- 12.4
P4 = {
 'title': "After the plague", 'sub': "persecution, wages and revolt, 1348 to 1450",
 'lede': "The Black Death left behind terror and opportunity. Jews were massacred as scapegoats, penitents whipped themselves in the streets, and the survivors, now scarce, demanded higher wages. Economists still argue over whether the plague set western Europe on a different path from the rest of the world.",
 'body': [
  "Panic sought culprits. Jews were accused of poisoning the wells, [[c-wells]] and in town after town they were killed: in Strasbourg the chronicler wrote that 'the money was indeed the thing that killed the Jews'. [[c-strasbourg]] The pope condemned the accusation, [[c-clement]] and one modern study suggests persecution was less likely where Jews were economically important. [[c-jjk-persecution]] Bands of flagellants, too, alarmed the Church. [[c-flagellants]]",
  "With so many dead, labour was scarce and wages rose. England tried to freeze them by law, [[c-statute]] and resentment helped spark the Peasants' Revolt of 1381, [[c-peasants]] whose preacher John Ball questioned the very idea of nobility. [[c-ball]] Over the following century serfdom faded in the West but hardened in the East. [[c-serfdom]]",
  "Did the plague make the West rich? Pamuk traces a wage gap between north-west Europe and the rest after 1450; [[c-pamuk]] Voigtländer and Voth argue high death rates kept incomes high; [[c-vv]] a recent survey finds the gains lasted only in some places, [[c-jjk-survey]] and the plague's effect on inequality is less simple than once thought. [[c-alfani]] Ancient DNA suggests it may even have left a mark on our immune systems. [[c-immune]]",
  {'table': {'head': ["Scholar", "Argument"], 'rows': [
    ["Şevket Pamuk (2007)", "wages held up in England and the Low Countries; a gap opened after 1450"],
    ["Voigtländer and Voth (2013)", "plague, war and cities kept death rates and incomes high"],
    ["Jedwab, Johnson and Koyama (2022)", "the wage rise lasted only in some parts of Europe"],
    ["Guido Alfani (2022)", "effects on inequality are 'much more complex'"],
    ["Robert Brenner", "economic models neglect 'class relationships and class conflicts'"]], 'note': "[[c-pamuk]] [[c-vv]] [[c-jjk-survey]] [[c-alfani]] [[c-serfdom]]"}}],
 'figure': {'kind': 'chart', 'chart': 'ledger', 'caption': "Two paths after the plague", 'title': "Labour and lordship in Europe, c. 1350-1600",
  'signs': False, 'hint': "Click an item",
  'left': {'h': "West of the Elbe", 'items': [
    {'t': "Wages rise", 's': "workers scarce after 1348 (12.4)"},
    {'t': "Laws to hold wages down", 's': "Ordinance (1349) and Statute (1351) of Labourers"},
    {'t': "Revolt", 's': "England, 1381"},
    {'t': "Serfdom fades", 's': "virtually extinct by c. 1500"}]},
  'right': {'h': "East of the Elbe", 'items': [
    {'t': "Lords tighten control", 's': "from the 15th century"},
    {'t': "A 'second serfdom'", 's': "harsher than the first"},
    {'t': "Lasts for centuries", 's': "15th to 18th centuries"}]},
  'notes': ["Sources: Ordinance of Labourers (Fordham; Avalon Project); Britannica; Munro (Toronto). Why the paths diverged is debated: see the table."]},
 'practice': [
  q("Which finding best supports the view that the plague's long-run economic effects depended on local conditions?",
    ["England and the Low Countries kept their high real wages", "Wages rose and then stayed high across the whole continent", "The Statute of Labourers held English wages at old levels", "Serfdom strengthened equally in western and eastern Europe"], 0,
    "Pamuk finds real wages held up best in England and the Low Countries, opening a gap after 1450, and a 2022 survey finds the rise 'only sustained in some parts of Europe'.",
    {1: "Jedwab, Johnson and Koyama find the rise was 'only sustained in some parts of Europe'.", 2: "The law tried to hold wages down, but Pamuk finds English real wages among those that held up best.", 3: "Serfdom faded in the West while a 'second serfdom' spread east of the Elbe."}),
  q("What does the Strasbourg chronicle suggest about the motives for the massacre of 1349?",
    ["Debts and Jewish property played a central part", "The killings were ordered by the pope at Avignon", "Most of Strasbourg's Jews had already died of plague", "Flagellants carried out the killings on papal orders"], 0,
    "The chronicler wrote that 'the money was indeed the thing that killed the Jews'.",
    {1: "The chronicle says the pope protected the Jews in Avignon, and Clement VI condemned the poisoning accusation.", 2: "The chronicle describes Jews being burned, about two thousand of them, not dying of disease.", 3: "Clement VI condemned the flagellants in 1349."})]}

# ---------------------------------------------------------------- 12.5
P5 = {
 'title': "Late medieval Latin Europe", 'sub': "war, schism and renewal, 1337 to 1455",
 'lede': "England and France fought for over a century, the Church split between rival popes, and reformers challenged its teachings. In Italy, scholars hunted for lost classical texts and bankers grew rich, and in Mainz a new way of printing began.",
 'body': [
  "The Hundred Years' War ended with England almost expelled from France. [[c-hyw]] In its course a young woman, Joan of Arc, raised the siege of Orléans, [[c-joan]] saying that saints had spoken to her. [[c-joan-voices]]",
  "The papacy, long resident at Avignon, split between rival popes until the Council of Constance restored a single one in 1417. [[c-schism]] The same council condemned the English theologian John Wyclif, whose followers translated the Bible into English, [[c-wyclif]] and sentenced the Czech reformer Jan Hus, who had come on King Sigismund's promise of safe-conduct; he was burned at the stake. [[c-hus]]",
  "In Italy, Petrarch searched monasteries for lost classical texts, [[c-petrarch]] and in 1422 the Florentine banker Giovanni di Bicci de' Medici became banker to the papacy. [[c-medici]] Around 1455 Johannes Gutenberg printed the Bible at Mainz, the start of a revolution covered in Chapter 13. [[c-gutenberg]]",
  {'table': {'head': ["Year", "Event"], 'rows': [
    ["1337", "Hundred Years' War begins"],
    ["1341", "Petrarch crowned poet laureate"],
    ["1378", "Western Schism begins"],
    ["1415", "Hus burned at Constance"],
    ["1417", "Martin V ends the schism"],
    ["1429-31", "Joan of Arc: Orléans to Rouen"],
    ["1453", "England keeps only Calais"],
    ["c. 1455", "Gutenberg Bible"]], 'note': "[[c-hyw]] [[c-petrarch]] [[c-schism]] [[c-hus]] [[c-joan]] [[c-gutenberg]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 5.5, 'lat': 47.5, 'zoom': 20}, 'caption': "Late medieval Latin Europe, 1337-1455", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [3.0, 45.3], 'label': 'FRANCE', 'size': 10}, {'ll': [-1.5, 52.4], 'label': 'ENGLAND', 'size': 9}, {'ll': [11.0, 49.6], 'label': 'EMPIRE', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [1.88, 50.25], 'label': 'Crécy', 'date': '1346', 'anchor': 'end', 'dy': 4},
    {'ll': [1.9, 47.9], 'label': 'Orléans', 'date': 'Joan, 1429', 'acc': True, 'dy': 16, 'plate': {'kicker': '12.5 · Joan of Arc', 'title': 'Joan of Arc', 'sub': '1429-1431', 'text': "[[c-joan]] [[c-joan-voices]] [[c-hyw]]", 'sources': ['brit-joan', 'brit-hyw']}},
    {'ll': [1.1, 49.44], 'label': 'Rouen', 'date': 'burned 1431', 'anchor': 'end', 'dy': -6},
    {'ll': [4.81, 43.95], 'label': 'Avignon', 'date': 'popes to 1377', 'acc': True, 'dy': 16, 'plate': {'kicker': '12.5 · the papacy', 'title': 'Avignon and the Schism', 'sub': '1378-1417', 'text': "[[c-schism]]", 'sources': ['brit-schism']}},
    {'ll': [9.18, 47.66], 'label': 'Constance', 'date': 'council, 1414-18', 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '12.5 · Constance', 'title': 'The Council of Constance', 'sub': '1414-1418', 'text': "[[c-schism]] [[c-wyclif]] [[c-hus]]", 'sources': ['brit-schism', 'brit-lollards', 'ht-wycliffe', 'brit-hus']}},
    {'ll': [8.27, 50.0], 'label': 'Mainz', 'date': 'Gutenberg, c. 1455', 'acc': True, 'dy': -8, 'plate': {'kicker': '12.5 · printing', 'title': 'The Gutenberg Bible', 'sub': 'c. 1455', 'text': "[[c-gutenberg]]", 'sources': ['loc-gutenberg']}},
    {'ll': [11.26, 43.77], 'label': 'Florence', 'date': 'the Medici', 'acc': True, 'dy': 16, 'plate': {'kicker': '12.5 · Italy', 'title': 'Petrarch and the Medici', 'sub': '14th-15th centuries', 'text': "[[c-petrarch]] [[c-medici]]", 'sources': ['uw-petrarch', 'brit-giovanni']}},
    {'ll': [-0.1, 51.52], 'label': 'London', 'date': 'revolt, 1381', 'anchor': 'end', 'dy': -6}]}]},
 'practice': [
  q("What did the Council of Constance (1414-18) achieve for the Church?",
    ["It ended the Western Schism by electing Martin V", "It moved the papacy back to Avignon from Rome", "It approved Wyclif's teaching and English Bible", "It sent Jan Hus home under Sigismund's safe-conduct"], 0,
    "After two and then three rival popes, the council elected Martin V in November 1417: a council resolved what rival popes could not.",
    {1: "The schism followed almost 70 years of popes at Avignon; Constance ended the schism.", 2: "Constance condemned Wyclif in 1415.", 3: "Hus came on that promise but was arrested, tried and burned on 6 July 1415."}),
  q("Which statement about the Gutenberg Bible is accurate?",
    ["The first book from movable metal type in western Europe", "The first book ever printed with movable metal type", "Printed in Florence and paid for by the Medici bank", "Printed as a single copy, for the pope at Rome"], 0,
    "Printed at Mainz in about 1455, in about 180 copies, it was the first book printed with movable metal type in western Europe.",
    {1: "Korean printers had used movable metal type about a century earlier.", 2: "It was printed at Mainz.", 3: "About 180 copies were printed."})]}

# ---------------------------------------------------------------- 12.6
P6 = {
 'title': "Iberia, 1250 to 1492", 'sub': "law, conversion and expulsion",
 'lede': "After Las Navas de Tolosa (see 11.3), Castile and Aragon came to share one royal couple from 1479, though each kept its own government. Their Jews suffered mass violence and forced conversion in 1391. In 1492 Ferdinand and Isabella took Granada and expelled the Jews who would not be baptised, and Portugal had already begun to sail down the coast of Africa.",
 'body': [
  "Alfonso X of Castile began a law code, the Siete Partidas, that shaped law in Spain and later in some of its former colonies. [[c-partidas]] In 1391 mobs in Seville and across the kingdoms killed thousands of Jews and forced others to convert, [[c-1391]] a turning point whose meaning historians now debate. [[c-1391-view]] Further pressure followed, as at the Disputation of Tortosa. [[c-tortosa]]",
  "The marriage of Isabella and Ferdinand in 1469 led to the union of the crowns of Castile and Aragon in 1479. [[c-isabella]] Suspicion of the conversos led to the Spanish Inquisition, [[c-inquisition]] and in 1492, three months after Granada surrendered, [[c-granada]] the monarchs ordered the Jews to leave, blaming their influence on the conversos. [[c-alhambra]] How many left is uncertain, [[c-expelled]] and modern Spain has revoked the decree and offered citizenship to descendants. [[c-alhambra-memory]]",
  "Portugal, meanwhile, turned outward: its princes took Ceuta in Morocco in 1415 and explored the Atlantic coast of Africa. [[c-henry]] The voyages of 1492 and after belong to Chapter 13.",
  {'table': {'head': ["Estimate of Jews leaving Spain, 1492", "Who"], 'rows': [
    ["40,000-50,000", "Gretchen Starr-LeBeau, drawing on Henry Kamen"],
    ["100,000", "Luis Suárez"],
    ["150,000-200,000", "'most contemporary historians', per a French university course"]], 'note': "[[c-expelled]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': -7.5, 'lat': 37.0, 'zoom': 13}, 'caption': "Iberia and the Atlantic, 1250-1492", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [-4.8, 39.2], 'label': 'CASTILE', 'size': 10}, {'ll': [0.0, 41.9], 'label': 'ARAGON', 'size': 9}, {'ll': [-8.0, 39.6], 'label': 'PORTUGAL', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [-5.99, 37.39], 'label': 'Seville', 'date': '1391; 1481', 'acc': True, 'big': True, 'anchor': 'end', 'dy': 4, 'plate': {'kicker': '12.6 · 1391', 'title': 'Seville', 'sub': '1391 and 1481', 'text': "[[c-1391]] [[c-1391-view]] [[c-inquisition]]", 'sources': ['fancy2014', 'brit-inq-timeline']}},
    {'ll': [0.52, 40.81], 'label': 'Tortosa', 'date': 'disputation, 1413-14', 'acc': True, 'dy': 16, 'plate': {'kicker': '12.6 · Tortosa', 'title': 'The Disputation of Tortosa', 'sub': '1413-14', 'text': "[[c-tortosa]]", 'sources': ['jvl-tortosa']}},
    {'ll': [-3.36, 40.48], 'label': 'Alcalá', 'date': 'Partidas recognised, 1348', 'acc': True, 'anchor': 'end', 'dy': -8, 'plate': {'kicker': '12.6 · law', 'title': 'The Siete Partidas', 'sub': 'begun under Alfonso X', 'text': "[[c-partidas]] [[c-isabella]]", 'sources': ['loc-partidas', 'brit-isabella']}},
    {'ll': [-3.6, 37.18], 'label': 'Granada', 'date': '2 January 1492', 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '12.6 · 1492', 'title': 'Granada and the expulsion', 'sub': '1492', 'text': "[[c-granada]] [[c-alhambra]] [[c-expelled]] [[c-alhambra-memory]]", 'sources': ['brit-muhammad12', 'cojs-alhambra', 'lemans-expulsion', 'enc-starrlebeau', 'loc-alhambra-blog', 'local-sephardic']}},
    {'ll': [-5.32, 35.89], 'label': 'Ceuta', 'date': '1415', 'acc': True, 'dy': 16, 'plate': {'kicker': '12.6 · Portugal', 'title': 'Henry the Navigator', 'sub': '1394-1460', 'text': "[[c-henry]]", 'sources': ['brit-henry']}},
    {'ll': [-16.91, 32.65], 'label': 'Madeira', 'dy': 16},
    {'ll': [-9.14, 38.72], 'label': 'Lisbon', 'anchor': 'end', 'dy': 4}]}]},
 'practice': [
  q("Why do estimates of the number of Jews who left Spain in 1492 vary so widely?",
    ["Historians differ on how many chose baptism instead", "Historians agree on 40,000 but disagree on the dates", "The decree was annulled before most Jews could leave", "Spain's 2015 law gives 72,199 as the number expelled"], 0,
    "Estimates run from 40,000-50,000 to 150,000-200,000; Gretchen Starr-LeBeau, drawing on Henry Kamen, notes that 'most converted rather than emigrated'.",
    {1: "Estimates run from 40,000-50,000 to 150,000-200,000.", 2: "Its deadline was the end of July 1492; Spain declared it without effect only in 1968.", 3: "72,199 is the number granted Spanish citizenship under that law by the end of 2024."}),
  q("Which link between events is best supported?",
    ["Suspicion of conversos shaped Inquisition and expulsion", "The attacks of 1391 began in newly conquered Granada", "The Inquisition targeted unbaptised Jews, not conversos", "Alfonso X's Siete Partidas ordered the expulsion of 1492"], 0,
    "Those baptised in 1391 and their descendants became the conversos; suspicion of them led to the Inquisition, and the decree of 1492 blames the 'interaction between the Jews and these Christians'.",
    {1: "The attacks began in Seville; Granada surrendered only in 1492.", 2: "Suspicion of the conversos, who were baptised Christians, led to the Inquisition.", 3: "Alfonso X died in 1284; the decree came from Ferdinand and Isabella."})]}

# ---------------------------------------------------------------- 12.7
P7 = {
 'title': "Timur and the Ottomans", 'sub': "1336 to 1481",
 'lede': "Timur, a conqueror from Central Asia, campaigned from India to Anatolia and strove to make Samarkand the most splendid city in Asia. At Ankara he captured the sultan of a rising Turkish dynasty, the Ottomans, and plunged it into civil war. The Ottomans recovered, and about half a century later took Constantinople, an event still contested in memory.",
 'body': [
  "Timur massacred whole cities in Iran and invaded India, [[c-timur]] while striving to make Samarkand, the capital of his realm, the most splendid city in Asia; its monuments of the Timurid age include the Bibi-Khanum mosque, the Gur-Emir mausoleum and Ulugh Beg's observatory. [[c-samarkand]] In 1402 he crushed the Ottomans at Ankara and captured their sultan. [[c-ankara]]",
  "The Ottomans had grown from a small principality in north-western Anatolia into a power on both sides of the Dardanelles. [[c-osman]] Why they grew so fast is debated, [[c-gaza]] but one institution was distinctive: the devshirme, which took Christian boys, converted them and trained them as soldiers and officials. [[c-devsirme]]",
  "On 29 May 1453 Mehmed II took Constantinople, ending the Roman empire in the east. [[c-1453]] He presented himself as heir to the Caesars as well as a champion of Islam. [[c-mehmed]] Hagia Sophia became a mosque, and in 2020 it became one again, to praise and protest. [[c-hagiasophia]]",
  {'table': {'head': ["Year", "Event"], 'rows': [
    ["after 1293", "Osman rules in north-western Anatolia"],
    ["1324 or 1326", "Bursa taken"],
    ["1354", "Gallipoli becomes a permanent Ottoman base in Europe"],
    ["1398", "Timur invades India"],
    ["1402", "Ankara: Bayezid I captured"],
    ["1405", "Timur dies at Otrar"],
    ["1453", "Constantinople taken"],
    ["2020", "Hagia Sophia a mosque again"]], 'note': "[[c-osman]] [[c-timur]] [[c-ankara]] [[c-1453]] [[c-hagiasophia]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 51.0, 'lat': 37.0, 'zoom': 5.5}, 'caption': "Timur and the Ottomans, 1354-1453", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [62.0, 37.0], 'label': 'TIMURID REALM', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [66.96, 39.65], 'label': 'Samarkand', 'date': "Timur's capital", 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '12.7 · Timur', 'title': 'Samarkand', 'sub': 'Timur, 1336-1405', 'text': "[[c-timur]] [[c-samarkand]]", 'sources': ['brit-timur', 'unesco-samarkand']}},
    {'ll': [68.3, 42.85], 'label': 'Otrar', 'date': 'Timur dies, 1405', 'dy': -6},
    {'ll': [77.2, 28.65], 'label': 'Delhi', 'date': 'invaded 1398', 'anchor': 'end', 'dy': 4},
    {'ll': [32.86, 39.93], 'label': 'Ankara', 'date': '20 July 1402', 'acc': True, 'dy': 16, 'plate': {'kicker': '12.7 · 1402', 'title': 'Ankara', 'sub': '20 July 1402', 'text': "[[c-ankara]]", 'sources': ['brit-ankara']}},
    {'ll': [29.06, 40.19], 'label': 'Bursa', 'date': '1324/26', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '12.7 · the Ottomans', 'title': 'Osman and Orhan', 'sub': 'c. 1293-1360', 'text': "[[c-osman]] [[c-gaza]] [[c-devsirme]]", 'sources': ['brit-osman-orhan', 'ostour-gaza', 'brit-devsirme']}},
    {'ll': [28.98, 41.01], 'label': 'Constantinople', 'date': '29 May 1453', 'acc': True, 'big': True, 'dy': -8, 'plate': {'kicker': '12.7 · 1453', 'title': 'The fall of Constantinople', 'sub': '29 May 1453', 'text': "[[c-1453]] [[c-mehmed]] [[c-hagiasophia]]", 'sources': ['brit-fall1453', 'brit-mehmed', 'sbs-hagiasophia']}}]}]},
 'practice': [
  q("What was the immediate consequence of the battle of Ankara (1402) for the Ottomans?",
    ["Bayezid was captured and his sons fought a civil war", "Timur went on to take Constantinople from the Byzantines", "Bayezid defeated Timur and went on to take Samarkand", "Timur made Ankara the new capital of his realm"], 0,
    "Bayezid I, the only Ottoman ruler ever captured by an enemy, was taken, and a civil war among his sons followed until 1413.",
    {1: "Constantinople fell to Mehmed II in 1453.", 2: "Timur won; Bayezid was captured.", 3: "Samarkand was the capital of Timur's realm."}),
  q("What is the debate over Paul Wittek's 'gaza thesis' about?",
    ["Whether holy war drove the early Ottomans' rapid growth", "Whether Wittek's critics proved holy war was the main motive", "Whether Osman's principality began in north-western Anatolia", "Whether Timur's victory at Ankara ended Ottoman expansion"], 0,
    "Wittek argued the Ottomans were driven by gaza, holy war against Christians; severe criticism from the 1980s left the thesis 'largely undermined'.",
    {1: "The reverse: the critics left Wittek's thesis 'largely undermined'.", 2: "That is not in dispute; the debate is about why the Ottomans grew so fast.", 3: "The gaza debate concerns the causes of the early growth; after Ankara the Ottomans recovered, and Mehmed II took Constantinople in 1453."})]}

PAGES = [P4, P5, P6, P7]
