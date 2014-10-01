

from CommonClasses import *
from solution import Solution


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
        self.test003()
        self.test004()
        self.test005()

    def test000(self):
        
        print 'test 000\n'
        
        S = 'barfoothefoobarman'
        L = ['foo','bar']
        startTime = time.clock()
        r = Solution().findSubstring(S, L)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(S, L)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        S = 'lingmindraboofooowingdingbarrwingmonkeypoundcake'
        L = ['fooo','barr','wing','ding','wing']
        startTime = time.clock()
        r = Solution().findSubstring(S, L)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(S, L)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        S = 'ccbabbaaab'
        L = ['aa','ba','bb']
        startTime = time.clock()
        r = Solution().findSubstring(S, L)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(S, L)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test003(self):
        
        print 'test 003\n'
        
        S = 'aaa'
        L = ['a', 'a']
        startTime = time.clock()
        r = Solution().findSubstring(S, L)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(S, L)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test004(self):
        
        print 'test 004\n'
        
        S = 'aaa'
        L = ['a', 'b']
        startTime = time.clock()
        r = Solution().findSubstring(S, L)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(S, L)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test005(self):
        
        print 'test 005\n'
        
        S = 'ejwwmybnorgshugzmoxopwuvshlcwasclobxmckcvtxfndeztdqiakfusswqsovdfwatanwxgtctyjvsmlcoxijrahivwfybbbudosawnfpmomgczirzscqvlaqhfqkithlhbodptvdhjljltckogcjsdbbktotnxgwyuapnxuwgfirbmdrvgapldsvwgqjfxggtixjhshnzphcemtzsvodygbxpriwqockyavfscvtsewyqpxlnnqnvrkmjtjbjllilinflkbfoxdhocsbpirmcbznuioevcojkdqvoraeqdlhffkwqbjsdkfxstdpxryixrdligpzldgtiqryuasxmxwgtcwsvwasngdwovxzafuixmjrobqbbnhwpdokcpfpxinlfmkfrfqrtzkhabidqszhxorzfypcjcnopzwigmbznmjnpttflsmjifknezrneedvgzfmnhoavxqksjreddpmibbodtbhzfehgluuukupjmbbvshzxyniaowdjamlfssndojyyephstlonsplrettspwepipwcjmfyvfybxiuqtkdlzqedjxxbvdsfurhedneauccrkyjfiptjfxmpxlssrkyldfriuvjranikluqtjjcoiqffdxaukagphzycvjtvwdhhxzagkevvuccxccuoccdkbboymjtimdrmerspxpktsmrwrlkvpnhqrvpdekmtpdfuxzjwpvqjjhfaupylefbvbsbhdncsshmrhxoyuejenqgjheulkxjnqkwvzznriclrbzryfaeuqkfxrbldyusoeoldpbwadhrgijeplijcvqbormrqglgmzsprtmryvkeevlthvflsvognbxfjilwkdndyzwwxgdbeqwlldyezmkopktzugxgkklimhhjqkmuaifnodtpredhqygmedtqpezboimeuyyujfjxkdmbjpizpqltvgknnlodtbhnbhjkmuhwxvzgmkhbcvvadhnssbvneecglnqxhavhvxpkjxlluilzpysjcnwguyofnhfvhaceztoiscumkhociglkvispihvyoatxcxbeqsmluixgsliatukrecgoldmzfhwkgaqzsckonjuhxdhqztjfxstjvikdrhpyjfxbjjryslfpqoiphrwfjqqhaamrjbrsiovrxmqsyxhqmritjeauwqbwtpqcqhvyyssvfknfhxvtodpzipueixdbntdfcaeatyyainfpkclbgaaqrwwzwbcjwiqzkwzfuxfclmsxpdyvfbnwxjytnaejivivriamhgqsskqhnqeurttrfrmstrbeokzhuzvbfmwywohmgogyhzpmsdemugqkspsmoppwbnwabdmiruibwznqcuczculujfiavzwynsyqxmarjkshjhxobandwyzggjibjgzyaaqxorqxbkenscbveqbaociwmqxxyzvyblypeongzrttvwqzmrccwkzidyfbxcaypyquodcpwxkstbthuvjqgialhfmgjohzoxvdaxuywfqrgmyahhtpqtazbphmfoluliznftodyguesshcacrsvutylalqrykehjuofisdookjhrljvedsywrlyccpaowjaqyfaqioesxnlkwgpbznzszyudpwrlgrdgwdyhucztsneqttsuirmjriohhgunzatyfrfzvgvptbgpwajgtysligupoqeoqxoyqtzozufvvlktnvahvsseymtpeyfvxttqosgpplkmxwgmsgtpantazppgnubmpwcdqkvhwfuvcahwibniohiqyywnuzzmxeppokxksrfwrpuzqhjgqryorwboxdauhrkxehiwaputeouwxdfoudcoagcxjcuqvenznxxnprgvhasffxtzaxpcfrcovwgrcwqptoekhmgpoywtxruxokcubekzcrqengviwbtgnzvdzrwwkqvacxwgdhffyvjldgvchoiwnfzoyvkiogisdfyjmfomcazigukqlumyzmnzjzhzfpslwsukykwckvktswjdqxdrlsqvsxwxpqkljeyjpulbswwmuhplfueqnvnhukgjarxlxvwmriqjgmxawmndhsvwnjdjvjtxcsjapfogpesxtpypenunfpjuyoevzztctecilqqbxkaqcyhiobvtqgqruumvvhxolbyzsqcrdchhdqprtkkjsccowrjtyjjmkhleanvfpemuublnnyzfabtxsestncfalqenfcswgerbfcqsapzdtscnzugmwlmidtxkvqhbuaecevwhmwkfqmvpgbefpqpsjmdecmixmmbsjxzwvjdmxydechlraajjmoqpcyoqmrjwoiumuzatydzcnktnkeyztoqvogodxxznhvzduzxudwwqhpftwdspuimioanlzobhjakgajafgzxpqckmhdbbnqmcszpuoqbztnftzgahhxwxbgkilnmzfydyxusnnvngksbjabqjaohdvrniezhmxmkxhemwbbclwdxwgngicplzgajmaryzfkyoqlkrmmfirchzrphveuwmvgaxzbwenvteifxuuefnimnadwxhruvoavlzyhfmeasmgrjawongccgfbgoualiaivbhcgvjjnxpggrewglalthmzvgziobrjeanlvyukwlscexbkibvdjhdgnepdiimmkcxhattwglbkicvsfswocbvphmtpwhcgjbnmxgidtlqcnnwtfujhvgzdussqbwynylzvtjapvqtidpdjkpshvrmqlhindhabubyokzdfrwqvnvgzkyhistydagsgnujiviyijdnabfxqbdqnexvwsvzvcsbrmkbkuzsdehghndyqjodnnblfwmaygdstotfkvxozgwhtbhlkvrzismnozqpfthajafuxekzlgigjpsukjvsdihrjzgovnreqwapdkoqswyclqyvbvpedzyoyedvuuamscbxnqnfmmjyehvidnoimmxmtcinwkbqmcobubjjpshucechrqrffqsyscnqoohcsxenypyqhfklloudgmklcejvgynwouzhtfwuuukdbwpmkjrqxeeaipxrokncholathupdetgaktmvmftqjvzyssocftjwemroghrncynmtchhhcaqxbqpthuaafwgrouaxonzocljeuslzsdwvuoodipdpnlhdihaywzmymxdjrqikughquwtenyucjdgrmipiidiwclhuepgyynoslhzahtdqwliktzsddaahohbszhqxxgripqlwlomjbwtuynydoakejmwkvojuwbfltqjfgxqhwkduzbxpdhtpvrzrfjndmsqfizmqxdxtpbpoemekvxzrrakwjxcxqsdasptruqmjtbaapgmkfnbwnlvzlxwdpzfjryanrmzmpzoefapmnsjdgecrdywsabctaegttffigupnwgakylngrrxurtotxqmzxvsqazajvrwsxyeyjteakeudzjxwbjvagnsjntskmocmpgkybqbnwvrwgoskzqkgffpsyhfmxhymqinrbohxlytsmoeleqrjvievpjipsgdkrqeuglrsjnmvdsihicsgkybcjltcswolpsfxdypmlbjotuxewskisnmczfgreuevnjssjifvlqlhkllifxrxkdbjlhcpegmtrelbosyajljvwwedtxbdccpnmreqaqjrxwulpunagwxesbilalrdniqbzxrbpcvmzpyqklsskpwctgqtrjwhrpisocwderqfiqxsdpkphjsapkvhvsqojyixaechvuoemmyqdlfkuzmlliugckuljfkljoshjhlvvlnywvjswvekfyqhjnsusefdtakejxbejrchoncklguqgnyrcslwztbstmycjziuskegagtlonducdogwbevugppsptdqbajmepmmizaycwcgmjeopbivsyphtvxvvgjbyxpgwpganjiaumojpyhhywosrmnouwpstgbrvhtlqcnmqbygbfnabesvshjmdbhyhirfrkqkmfwdgujhzyjdcbyuijjnkqluaczrnrbbwaeeupnwqzbsazplkyaxqorqsshhlljjlpphhedxdepgfgrqerpuhgmaawhnhqwsgnznrfmxjbdrkwjopylxezxgvetcvrwdewsxdeumhzfrvoilmvksuhyqltuimrnsphqslmgvmmojawwptghonigbdclqtbikiacwpjrbxhmzejozpypfixglatdvuogdoizdtsgsztsfcihtgwyqugeuahpuvvzmgarbsyuutmbxuisdfrvbxzxzhmuektssuktoknkfbmcwwubbnwenybmfqglaceuyqnoadzfenjcjfdlvcpiatuhjdujhaffqsvqvuxchgerokejovrqonxxstibunikiedfyahijobxyhimebctobsjudkqstbcxgixgrhpfiofpwruzvpqyjzvollheoldutddnksutjakhtghpxxnjykxjwgqmsvhnykclexepxqxqzghwfxfdhfmflesfabvanxlrurjtigkjotftqnwyskffpxlragrnfffawqtgyfpmzxfpkdpenxlewyxxgrkmwrmshhzfnorolyfxbvdrspxqnxnuoygkruczddgssygfymdcjgvdxutlrhffhnpyjuxmxefrelxezcgikdliyhvpocvvpkvagvmezrxffujeysplvavtjqjxsgujqsjznxforctwzecxyrkwufpdxadrgzczrnyelfschnagucguuqqqwitviynrypsrdswqxqsegulcwrwsjnihxedfcqychqumiscfkwmqqxunqrfbgqjdwmkyelbldxympctbzfupeocwhkypchuyvhybsbmvymjppfrqmlfrbkpjwpyyytytawuuyjrwxboogfessmltwdcssdqtwomymjskujjtmxiueopwacrwfuqazitvyhvlspvoaeipdsjhgyfjbxhityisidnhlksfznubucqxwaheamndjxmcxwufajmnveuwuoyosqnoqwvtjkwuhkzghvmjhawcfszbhzrbpgsidnbmxxihihnrfbamcyojqpkzodbejtmmipahojoysepzhpljpaugrghgjimtdahnpivdtlcnptnxjyiaafislqavamqgmxtdfoiaakorebqpbbpegawrqymqkewycsdjglkiwaacdqterkixkgraedtqirqmjtvsfhadhafktyrmkzmvidxmisfskvevpcnujqxrqedleuyowkjgphsxzzqlvujkwwgiodbfjesnbsbzcnftuzrvzjjudsgcqmmfpnmyrenuxotbbyvxyovzxgtcyzgqnsvcfhczoptnfnojnlinbfmylhdlijcvcxzjhdixuckaralemvsnbgooorayceuedtomzyjtctvtwgyiesxhynvogxnjdjphcftbefxgasawzagfugmuthjahylkhatlgpnkuksuesrduxkodwjzgubpsmzzmvkskzeglxaqrrvmrgcwcnvkhwzbibaxwnriowoavosminabvfxastkcrkdclgzjvqrjofjjvbyfragofeoazzeqljuypthkmywaffmcjkickqqsuhsviyovhitxeajqahshpejaqtcdkuvgdpclnsguabtgbfwdmrmbvydorfrbcokfdmtsgboidkpgpnmdeyhawkqqshtwxdbarwuxykgduxjlkxppwyruihkcqgynjcpbylayvgdqfpbqmshksyfbhrfxxemhgbkgmkhjtkzyzdqmxxwqvdtevyducpdksntgyaqtkrrkwiyuhukfadjvdnrievszilfinxbyrvknfihmetreydbcstkwoexwsfhfekfvfplmxszcosgovisnbemrjlndqwkvhqsofdbdychmupcsxvhazvrihhnxfyumonbvqeyoghccxfuwacxzxqkezxefxarnnujgyjugrzjoefmghjfhcrnbrtgouaehwnnxwkdplodpuqxdbemfwahptpfppjzowoltyqijfoabgzejerpatwponuefgdtcrgxswiddygeeflpjeelzccnsztxfyqhqyhkuppapvgvdtkmxraytcolbhkiiasaazkvqzvfxbaaxkoudovxrjkusxdazxaawmvoostlvvnsfbpjqkijvudpriqrfsrdfortimgdhtypunakzituezjyhbrpuksbamuiycngvlvpyvczfxvlwhjgicvempfobbwadkiavdswyuxdttoqaaykctprkwfmyeodowglzyjzuhencufcwdobydslazxadnftllhmjslfbrtdlahkgwlebdpdeofidldoymakfnpgekmsltcrrnxvspywfggjrmxryybdltmsfykstmlnzjitaipfoyohkmzimcozxardydxtpjgquoluzbznzqvlewtqyhryjldjoadgjlyfckzbnbootlzxhupieggntjxilcqxnocpyesnhjbauaxcvmkzusmodlyonoldequfunsbwudquaurogsiyhydswsimflrvfwruouskxjfzfynmrymyyqsvkajpnanvyepnzixyteyafnmwnbwmtojdpsucthxtopgpxgnsmnsrdhpskledapiricvdmtwaifrhnebzuttzckroywranbrvgmashxurelyrrbslxnmzyeowchwpjplrdnjlkfcoqdhheavbnhdlltjpahflwscafnnsspikuqszqpcdyfrkaabdigogatgiitadlinfyhgowjuvqlhrniuvrketfmboibttkgakohbmsvhigqztbvrsgxlnjndrqwmcdnntwofojpyrhamivfcdcotodwhvtuyyjlthbaxmrvfzxrhvzkydartfqbalxyjilepmemawjfxhzecyqcdswxxmaaxxyifmouauibstgpcfwgfmjlfhketkeshfcorqirmssfnbuqiqwqfhbmol'
        L = ['toiscumkhociglkvispihvyoatxcx','ndojyyephstlonsplrettspwepipw','yzfkyoqlkrmmfirchzrphveuwmvga','mxxihihnrfbamcyojqpkzodbejtmm','fenjcjfdlvcpiatuhjdujhaffqsvq','ehghndyqjodnnblfwmaygdstotfkv','heoldutddnksutjakhtghpxxnjykx','cvrwdewsxdeumhzfrvoilmvksuhyq','ftqjvzyssocftjwemroghrncynmtc','idiwclhuepgyynoslhzahtdqwlikt','eurttrfrmstrbeokzhuzvbfmwywoh','jxlluilzpysjcnwguyofnhfvhacez','uskegagtlonducdogwbevugppsptd','xmcxwufajmnveuwuoyosqnoqwvtjk','wolpsfxdypmlbjotuxewskisnmczf','fjryanrmzmpzoefapmnsjdgecrdyw','jgmxawmndhsvwnjdjvjtxcsjapfog','wuhkzghvmjhawcfszbhzrbpgsidnb','yelbldxympctbzfupeocwhkypchuy','vzduzxudwwqhpftwdspuimioanlzo','bdpdeofidldoymakfnpgekmsltcrr','fmyeodowglzyjzuhencufcwdobyds','dhtypunakzituezjyhbrpuksbamui','bdmiruibwznqcuczculujfiavzwyn','eudzjxwbjvagnsjntskmocmpgkybq','tuynydoakejmwkvojuwbfltqjfgxq','psrdswqxqsegulcwrwsjnihxedfcq','cokfdmtsgboidkpgpnmdeyhawkqqs','fujhvgzdussqbwynylzvtjapvqtid','rqeuglrsjnmvdsihicsgkybcjltcs','vhybsbmvymjppfrqmlfrbkpjwpyyy','aukagphzycvjtvwdhhxzagkevvucc','hwkduzbxpdhtpvrzrfjndmsqfizmq','ywnuzzmxeppokxksrfwrpuzqhjgqr','qbajmepmmizaycwcgmjeopbivsyph','uamscbxnqnfmmjyehvidnoimmxmtc','nxvspywfggjrmxryybdltmsfykstm','amrjbrsiovrxmqsyxhqmritjeauwq','yorwboxdauhrkxehiwaputeouwxdf','qkewycsdjglkiwaacdqterkixkgra','ycngvlvpyvczfxvlwhjgicvempfob','jgphsxzzqlvujkwwgiodbfjesnbsb','mkxhemwbbclwdxwgngicplzgajmar','mryvkeevlthvflsvognbxfjilwkdn','mezrxffujeysplvavtjqjxsgujqsj','rtotxqmzxvsqazajvrwsxyeyjteak','sabctaegttffigupnwgakylngrrxu','xccuoccdkbboymjtimdrmerspxpkt','xusnnvngksbjabqjaohdvrniezhmx','oyuejenqgjheulkxjnqkwvzznricl','mxszcosgovisnbemrjlndqwkvhqso','wsgnznrfmxjbdrkwjopylxezxgvet','dxmisfskvevpcnujqxrqedleuyowk','dhrgijeplijcvqbormrqglgmzsprt','vuxchgerokejovrqonxxstibuniki','lumyzmnzjzhzfpslwsukykwckvkts','inwkbqmcobubjjpshucechrqrffqs','ywtxruxokcubekzcrqengviwbtgnz','ccpnmreqaqjrxwulpunagwxesbila','pesxtpypenunfpjuyoevzztctecil','sygfymdcjgvdxutlrhffhnpyjuxmx','uisdfrvbxzxzhmuektssuktoknkfb','cejvgynwouzhtfwuuukdbwpmkjrqx','oudcoagcxjcuqvenznxxnprgvhasf','sxnlkwgpbznzszyudpwrlgrdgwdyh','qqbxkaqcyhiobvtqgqruumvvhxolb','mkhleanvfpemuublnnyzfabtxsest','bibaxwnriowoavosminabvfxastkc','bcxgixgrhpfiofpwruzvpqyjzvoll','lzccnsztxfyqhqyhkuppapvgvdtkm','pdjkpshvrmqlhindhabubyokzdfrw','qbbnhwpdokcpfpxinlfmkfrfqrtzk','rnyelfschnagucguuqqqwitviynry','qtrjwhrpisocwderqfiqxsdpkphjs','vxttqosgpplkmxwgmsgtpantazppg','tyisidnhlksfznubucqxwaheamndj','kgaqzsckonjuhxdhqztjfxstjvikd','jeuslzsdwvuoodipdpnlhdihaywzm','vdzrwwkqvacxwgdhffyvjldgvchoi','cftbefxgasawzagfugmuthjahylkh','xraytcolbhkiiasaazkvqzvfxbaax','oyqtzozufvvlktnvahvsseymtpeyf','rnnujgyjugrzjoefmghjfhcrnbrtg','rfzvgvptbgpwajgtysligupoqeoqx','igbdclqtbikiacwpjrbxhmzejozpy','dyzwwxgdbeqwlldyezmkopktzugxg','hmetreydbcstkwoexwsfhfekfvfpl','zcnftuzrvzjjudsgcqmmfpnmyrenu','zzmvkskzeglxaqrrvmrgcwcnvkhwz','vjswvekfyqhjnsusefdtakejxbejr','rwwzwbcjwiqzkwzfuxfclmsxpdyvf','fdbdychmupcsxvhazvrihhnxfyumo','vdtevyducpdksntgyaqtkrrkwiyuh','nbvqeyoghccxfuwacxzxqkezxefxa','vpgbefpqpsjmdecmixmmbsjxzwvjd','jwgqmsvhnykclexepxqxqzghwfxfd','olyfxbvdrspxqnxnuoygkruczddgs','qgmxtdfoiaakorebqpbbpegawrqym','liaivbhcgvjjnxpggrewglalthmzv','choncklguqgnyrcslwztbstmycjzi','fpkdpenxlewyxxgrkmwrmshhzfnor','hhhcaqxbqpthuaafwgrouaxonzocl','ipahojoysepzhpljpaugrghgjimtd','wosrmnouwpstgbrvhtlqcnmqbygbf','nwyskffpxlragrnfffawqtgyfpmzx','bcvvadhnssbvneecglnqxhavhvxpk','hoavxqksjreddpmibbodtbhzfehgl','lazxadnftllhmjslfbrtdlahkgwle','uuukupjmbbvshzxyniaowdjamlfss','tpqtazbphmfoluliznftodyguessh','ychqumiscfkwmqqxunqrfbgqjdwmk','rkdclgzjvqrjofjjvbyfragofeoaz','pphhedxdepgfgrqerpuhgmaawhnhq','cacrsvutylalqrykehjuofisdookj','kyldfriuvjranikluqtjjcoiqffdx','bnwvrwgoskzqkgffpsyhfmxhymqin','uzmlliugckuljfkljoshjhlvvlnyw','abfxqbdqnexvwsvzvcsbrmkbkuzsd','xotbbyvxyovzxgtcyzgqnsvcfhczo','bwtpqcqhvyyssvfknfhxvtodpzipu','nsfbpjqkijvudpriqrfsrdfortimg','tgwyqugeuahpuvvzmgarbsyuutmbx','upnwqzbsazplkyaxqorqsshhlljjl','edfyahijobxyhimebctobsjudkqst','ialhfmgjohzoxvdaxuywfqrgmyahh','jlhcpegmtrelbosyajljvwwedtxbd','tpfppjzowoltyqijfoabgzejerpat','mgogyhzpmsdemugqkspsmoppwbnwa','nubmpwcdqkvhwfuvcahwibniohiqy','ukfadjvdnrievszilfinxbyrvknfi','dgnepdiimmkcxhattwglbkicvsfsw','syqxmarjkshjhxobandwyzggjibjg','bnwxjytnaejivivriamhgqsskqhnq','hzyjdcbyuijjnkqluaczrnrbbwaee','yscnqoohcsxenypyqhfklloudgmkl','habidqszhxorzfypcjcnopzwigmbz','wjdqxdrlsqvsxwxpqkljeyjpulbsw','tytawuuyjrwxboogfessmltwdcssd','pfixglatdvuogdoizdtsgsztsfcih','apkvhvsqojyixaechvuoemmyqdlfk','ouaehwnnxwkdplodpuqxdbemfwahp','ixuckaralemvsnbgooorayceuedto','ymxdjrqikughquwtenyucjdgrmipi','smrwrlkvpnhqrvpdekmtpdfuxzjwp','bhjakgajafgzxpqckmhdbbnqmcszp','beqsmluixgsliatukrecgoldmzfhw','greuevnjssjifvlqlhkllifxrxkdb','yzsqcrdchhdqprtkkjsccowrjtyjj','sviyovhitxeajqahshpejaqtcdkuv','qtwomymjskujjtmxiueopwacrwfuq','mzyjtctvtwgyiesxhynvogxnjdjph','dyfbxcaypyquodcpwxkstbthuvjqg','hfmflesfabvanxlrurjtigkjotftq','mxydechlraajjmoqpcyoqmrjwoium','nabesvshjmdbhyhirfrkqkmfwdguj','bhrfxxemhgbkgmkhjtkzyzdqmxxwq','gziobrjeanlvyukwlscexbkibvdjh','mcwwubbnwenybmfqglaceuyqnoadz','xyzvyblypeongzrttvwqzmrccwkzi','ncfalqenfcswgerbfcqsapzdtscnz','dtqpezboimeuyyujfjxkdmbjpizpq','wmuhplfueqnvnhukgjarxlxvwmriq','qwapdkoqswyclqyvbvpedzyoyedvu','uoqbztnftzgahhxwxbgkilnmzfydy','zsddaahohbszhqxxgripqlwlomjbw','bwadkiavdswyuxdttoqaaykctprkw','eixdbntdfcaeatyyainfpkclbgaaq','nmjnpttflsmjifknezrneedvgzfmn','avlzyhfmeasmgrjawongccgfbgoua','kklimhhjqkmuaifnodtpredhqygme','xzbwenvteifxuuefnimnadwxhruvo','ugmwlmidtxkvqhbuaecevwhmwkfqm','rhpyjfxbjjryslfpqoiphrwfjqqha','eeaipxrokncholathupdetgaktmvm','ltuimrnsphqslmgvmmojawwptghon','azitvyhvlspvoaeipdsjhgyfjbxhi','efrelxezcgikdliyhvpocvvpkvagv','znxforctwzecxyrkwufpdxadrgzcz','kcqgynjcpbylayvgdqfpbqmshksyf','hrljvedsywrlyccpaowjaqyfaqioe','cjmfyvfybxiuqtkdlzqedjxxbvdsf','zeqljuypthkmywaffmcjkickqqsuh','wnfzoyvkiogisdfyjmfomcazigukq','zyaaqxorqxbkenscbveqbaociwmqx','ahnpivdtlcnptnxjyiaafislqavam','edtqirqmjtvsfhadhafktyrmkzmvi','wponuefgdtcrgxswiddygeeflpjee','xozgwhtbhlkvrzismnozqpfthajaf','ptnfnojnlinbfmylhdlijcvcxzjhd','uxekzlgigjpsukjvsdihrjzgovnre','rbohxlytsmoeleqrjvievpjipsgdk','fxtzaxpcfrcovwgrcwqptoekhmgpo','tvxvvgjbyxpgwpganjiaumojpyhhy','vqjjhfaupylefbvbsbhdncsshmrhx','urhedneauccrkyjfiptjfxmpxlssr','ltvgknnlodtbhnbhjkmuhwxvzgmkh','ucztsneqttsuirmjriohhgunzatyf','rbzryfaeuqkfxrbldyusoeoldpbwa','atlgpnkuksuesrduxkodwjzgubpsm','lrdniqbzxrbpcvmzpyqklsskpwctg','qvnvgzkyhistydagsgnujiviyijdn','uzatydzcnktnkeyztoqvogodxxznh','ocbvphmtpwhcgjbnmxgidtlqcnnwt','koudovxrjkusxdazxaawmvoostlvv','ptruqmjtbaapgmkfnbwnlvzlxwdpz','xdxtpbpoemekvxzrrakwjxcxqsdas','gdpclnsguabtgbfwdmrmbvydorfrb','htwxdbarwuxykgduxjlkxppwyruih']
        startTime = time.clock()
        r = Solution().findSubstring(S, L)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(S, L)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print
    

def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    