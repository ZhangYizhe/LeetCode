from typing import List

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        def check(subString: str) -> int:
            count = 0
            for char in subString:
                if char in vowels:
                    count += 1
            return count

        l = 0
        r = k - 1

        countVowels = check(s[l:r + 1])
        maxCountVowels = countVowels

        while r < len(s) - 1:
            r += 1

            l_is = True if s[l] in vowels else False
            r_is = True if s[r] in vowels else False

            if l_is and not r_is:
                countVowels -= 1
            elif not l_is and r_is:
                countVowels += 1

            if countVowels > maxCountVowels:
                maxCountVowels = countVowels

            l += 1

        return maxCountVowels



s = "eyqfwxejdgqsfrxppfesxwwgmjkcdlnafmsloxktemyykdlexuszckgwqklzkqeduqmjrkgetgktnjzxlzkqaflzvgxxygotmlzoiznsavtnbbkwuciuijnfsyzanzrfsuzcnuxiejxocgowbirlmvmujrzmssmtovqbrdceacokcoekemyideroycqwnbzozqkwlivlavqbxrlgpednyibmweznajgtypzrorympnphrpbuqywxrlpqsubrrsoaquhzamavrhvstgwcofxnxiijptxthtnfpzijuxcqeyttsjiqypzutygshhsizeeuyqzrqotcyekrovvqdwvgxjtfihozwhpeztsoguofdwfyhesgmhnuvhzpgdgunzsronzvhlilpkiaruejxtzxciqiixuwfktrgwfhfelvdxfalsvhgnsvcypbccoafqkkkdvlvpjpoyufklbyjvucmkpdqialsjjqqrroivvbgrwcluuelcrzmiamufplhmiadkbuiivcbczcatvthjwlowpvilhiqekysropezzgefnvryksznsssgjivllckhjafgnubloyoqzixneyndixatrganzpazrjdedvqswzejocoeehdfsxndellurlbhnxvbktrvzzsyrcyvygcdhmmfxpdjfcajibegawzztpwdwivypgrkvxzljmxavzslbelffnuugnreagptghwaibzvofcerpikouqksygnaexuudsohppeylclwocfchtlcbcqxcdxdexfizekctlgwlkfaemwutgyvtgdomvykxrsbjtipwlqexgfxhmsvhxkwbkmetgqyltwtfesurcivukeebjjuqpuavsyecucemqfeiwoboqjulnkunrlsyttmnvrbshtvyyvjmlzjddcqhpygpxjgdogxyzorcnwdobulsfpqbbmmxbhmsiyrkdltxifmhuotomyxqyezkalbvodllzrsedqudoffgygryljohhiiffmyzpwtyeydanskabfmgplbkjimoxodznupyxtpopccrlwbusxetxpkgkrmjvwfrbmuwzrmjrjenteemvztmydvuxxdfzahvcmgyqkgeufrlbdirnexaessqyighgrtczmzwhrizjidxwnsqhxfpjkjzzideqabwzlawtgiisahqwsbirbrhgmsbqnrfvbzvdjiemllneeixgtbdeuhplhphwsawbjwmhuqmbeqpugvtkvuomueepjmxmezlfhjsoawfizessuumxfdfsikdbyqbsagxhkpisdsiiidahgirovwoyjlgerfdfoqjqdqosjlimaiwlaaojehatmmavobfffnzzofumssocomltakusufbzpnxsiyqoubkurtfgpbqqtgsvfzghvosrlbxuwcrudiyvtaxthmxtaevugoxomyydblwfovxytzqxhidtwookvutgtjmbkiwlvdcgjdrlgsnzdafxyzhndtozclgfgplovloepwzzydfbrlertatbbxzjohnhfqsgwrbokvgcvdnyuatqarnnzambfaohwbqkpoykvjxvujuaxdprelkdexsgmtqisxfghkpkhntnnrnoorpffhapdlqwhybdmxwwzvvboepqyripddpgdfcfvgygsnenurwhnwgysushnokcdeeucffyrntchvcmytexcouhyymohkhddlneijkopbbfdlcfpeotpcvpaptyufnytscvrywrkbiwjmuiwzfuwcqipsuedwwiocdjnlomgodtmfaphrygtyputhhdieywrdiiwainiuxupsqpxpsmwsfsfpffhefpstiwdsoxhebmmjafbsmtczeuifivdezbwaszuzfhwslucfkrhrmwxkvxaieinasenkdupfqxovsulxourphthletosqqqwocksnqrjvfrnlpsyaxebzcgosqmnrpfznmdvuqkwrdggeqjgdnfyumbwovsylwsorxqzhqmqpqpvsqakpymrqgxwjbnxswnnemesyfbrezwtdfjcmzqeorpkvbsjvahnofncksxkyugmmvhnqbcseajkwnpkrmsgfzonehyrblfzlamkahmmyqdgtlqtfvbeztczgkxyzhpogozwimfmompywtbsyjhjbiokfwtcswpcifsgkekjbtgzlzftpqicmpryjapwmwqaalnaysahdueeiyxpfrlwokzymbgljvidwowokoehktwroyxppwdehdeamkiqexjngoumxvqfnvlrdltcsogwuhazbnzzjkoduugcjyatgwrginmwvsfcidryxabmwjmdjjohranxbonozbottqxsmyehdfadgzmvlpappotqhurukyazmkfbspwxwxzvmaleptjnyitrazfufnldvmlycqnagbilghcfctxtwvaujdctoitubkbtvzyecvsrijcotvbsnmdobxdjkzrvyxxfpfycnnbywhquayjsbniopfzugnzfnybvxuqumezkwcyawgrdybumllvbptdssalaufwtsojslnurhmcfdcpayeunblgpmxdjxoijzdvihcnnrqkkgsugeovsfgrcjzihshmrqbjzvymioxnjkmdcabrfwqnizmnemcimtbghwqclleuofymhdhrgtzdpfewjbztdbmyymwkicnmnscekndavbsfycywwgmheudxmnqublscexgyalevrftowleubvelwoqjciivffrlwsinkawmmxdvkbezwwhlytegoxbxaxwasfiawjnrtuceazntbvitqariwseltrstbrhcmzreianyhodtfowbuddiggsekqnxbaozpmsxsgzrhztheqvgfpjtdcdzazidhphbhnvd"
k = 746

print(Solution().maxVowels(s, k))