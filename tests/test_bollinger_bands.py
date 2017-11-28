from __future__ import absolute_import
import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import bollinger_bands


class TestBollingerBands(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.upper_bb_period_6_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, 816.52449933994092, 814.27550939504749, 816.54237371875843,
        815.99126278552046, 815.99290069955305, 817.15420069693744,
        819.17174199421459, 819.54594831881377, 820.13633012774312,
        820.1788881276284, 825.44308751353708, 825.73590328428679,
        825.6732523285624, 818.89776666045145, 815.09000697647843,
        802.09929833664626, 793.50535591112305, 791.9876616255375,
        795.50243136837298, 796.01708505294425, 795.05267417812718,
        791.73810897161934, 791.0558772214913, 789.07567422681598,
        789.27660584599676, 789.27437711598964, 790.02222702081929,
        797.73049399344904, 794.12246338282625, 795.40783812003292,
        808.55054947975941, 823.26717226480605, 829.21235190390985,
        822.12771893870047, 819.88675270042563, 819.02597753057012,
        818.97581684541399, 817.68218544834099, 827.09430820011494,
        831.81127725910437, 833.22277441389804, 832.41143058559442,
        838.64072585583324, 836.78560700606158, 836.65429643283642,
        836.15308903008849, 836.2472753828082, 840.03702032786532,
        834.89915668048775, 832.96449074206055, 830.1461799602198,
        821.53110435325709, 815.87559699074632, 816.90725796989284,
        817.02476731049114, 817.35782823904401, 815.11601674386236,
        813.27976505875324, 804.73797072139701, 804.79492174879806,
        809.82343479713552, 812.9008322191321, 812.90593915342788,
        816.88370580516846, 820.05682701798787, 819.52994002288142,
        820.40100177793533, 820.72350371582672, 820.92948012976728,
        815.90917059380342, 807.47915844920715, 804.85031607621283,
        804.42463737840717, 804.66191376063853, 807.12996342695999,
        811.2394847169287, 815.33514412124453, 814.13187527866114,
        814.53027771458801, 814.1345662504051, 812.90200561502502,
        807.76138315346714, 798.10829923333938, 796.00929742139624,
        796.40124960990579, 797.57180011371815, 798.64308585519279,
        800.78522853822278, 804.2936034382858, 807.10642057784503,
        806.66061544677029, 808.29119061556412, 809.01716124063353,
        809.92993881381472, 810.92340033024971, 811.33021698273387,
        809.38917848590643, 809.34556139121514, 813.35444699067409,
        812.75716945970373, 810.72871661628039, 808.41137860478068,
        808.53340454790157, 816.9661407886357, 819.18411894583403,
        816.12382431443473, 806.83548339067977, 789.32359444378812,
        766.72866894726383, 762.56650994032907, 760.58520005021819,
        760.37076616296906, 767.57066829340431, 766.16792550087803,
        765.58397542355704, 759.28496109954585, 752.51575300318245,
        742.07969942038721, 744.40923235619834, 740.28851380721312,
        737.24034787019923, 727.92495065781475]

        self.middle_bb_period_6_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, 804.55166666666673, 807.84333333333336, 809.89666666666665,
        811.21833333333325, 811.20333333333338, 812.51166666666666,
        813.88000000000011, 814.40333333333331, 813.18666666666661,
        812.6783333333334, 810.23333333333346, 806.20333333333338,
        799.25166666666667, 793.06499999999994, 785.82499999999993,
        778.30499999999995, 775.09000000000003, 774.75166666666667,
        776.35333333333347, 776.68333333333339, 779.10666666666668,
        782.55166666666673, 784.03833333333341, 781.79333333333341,
        781.85500000000002, 781.81833333333327, 781.17833333333328,
        775.88166666666666, 773.70666666666659, 774.42666666666662,
        777.66499999999996, 782.99833333333333, 787.4766666666668,
        792.12333333333345, 793.86333333333334, 795.21833333333336,
        795.20000000000016, 794.85333333333335, 797.77499999999998,
        803.81666666666672, 810.46833333333336, 817.15666666666664,
        822.19999999999993, 824.55999999999983, 824.90499999999986,
        826.52833333333331, 826.42666666666662, 822.80833333333339,
        817.61833333333345, 814.28833333333341, 812.64499999999998,
        809.72499999999991, 808.505, 807.48333333333323, 807.23000000000002,
        806.75500000000011, 805.25833333333321, 803.72666666666657,
        802.04166666666663, 802.36333333333334, 803.52666666666664,
        805.11000000000001, 805.08666666666659, 807.51666666666677,
        809.49833333333333, 809.89666666666665, 808.18333333333328,
        805.62666666666667, 804.84666666666669, 802.55833333333339,
        798.31000000000006, 795.5916666666667, 795.43166666666673,
        794.28000000000009, 795.0916666666667, 796.21833333333336,
        799.1450000000001, 800.50333333333344, 799.26666666666677, 799.495,
        797.67500000000007, 795.64666666666665, 793.17999999999995,
        792.25166666666667, 792.61833333333345, 793.74166666666667,
        794.58000000000004, 795.21833333333325, 796.80666666666673,
        799.15999999999997, 800.42500000000007, 801.98666666666668,
        803.67000000000007, 805.09499999999991, 806.05166666666662,
        806.39499999999987, 807.06833333333327, 807.23000000000002,
        805.59666666666669, 804.04999999999984, 802.65500000000009,
        801.56499999999994, 799.25, 792.40166666666664, 786.52166666666665,
        779.64333333333332, 772.54333333333341, 765.60000000000002,
        759.44500000000005, 757.98500000000001, 756.55833333333328,
        755.81666666666661, 752.16833333333341, 748.25500000000011,
        744.10000000000002, 740.005, 735.63666666666666, 729.73333333333323,
        725.005, 720.53333333333342, 716.43500000000006, 712.72500000000002]

        self.lower_bb_period_6_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, 792.57883399339255, 801.41115727161923, 803.25095961457487,
        806.44540388114604, 806.4137659671137, 807.86913263639588,
        808.58825800578563, 809.26071834785284, 806.2370032055901,
        805.1777785390384, 795.02357915312984, 786.67076338237996,
        772.83008100477093, 767.23223333954843, 756.55999302352143,
        754.51070166335364, 756.67464408887702, 757.51567170779583,
        757.20423529829395, 757.34958161372253, 763.16065915520619,
        773.36522436171413, 777.02078944517552, 774.51099243985084,
        774.43339415400328, 774.36228955067691, 772.33443964584728,
        754.03283933988428, 753.29086995050693, 753.44549521330032,
        746.77945052024052, 742.72949440186062, 745.74098142942375,
        762.11894772796643, 767.83991396624106, 771.41068913609661,
        771.42418315458633, 772.02448121832572, 768.45569179988502,
        775.82205607422907, 787.71389225276869, 801.90190274773886,
        805.75927414416662, 812.33439299393808, 813.1557035671633,
        816.90357763657812, 816.60605795052504, 805.57964633880147,
        800.33750998617916, 795.61217592460628, 795.14382003978017,
        797.91889564674273, 801.13440300925367, 798.05940869677363,
        797.43523268950889, 796.15217176095621, 795.40064992280406,
        794.17356827457991, 799.34536261193625, 799.93174491786863,
        797.22989853619777, 797.31916778086793, 797.2673941799053,
        798.14962752816507, 798.9398396486788, 800.26339331045187,
        795.96566488873123, 790.52982961750661, 788.7638532035661,
        789.20749607286336, 789.14084155079297, 786.33301725712056,
        786.43869595492629, 783.89808623936165, 783.0533699063734,
        781.19718194973802, 782.95485587875567, 786.87479138800575,
        784.00305561874552, 784.85543374959491, 782.44799438497512,
        783.53195017986616, 788.25170076666052, 788.49403591193709,
        788.83541705676112, 789.91153321961519, 790.51691414480729,
        789.65143812844371, 789.31972989504766, 791.21357942215491,
        794.18938455322984, 795.68214271776924, 798.32283875936662,
        800.26006118618511, 801.17993300308353, 801.45978301726586,
        804.74748818076012, 805.11443860878489, 797.83888634265929,
        795.34283054029595, 794.58128338371978, 794.7186213952192,
        789.96659545209843, 767.83719254469759, 753.85921438749926,
        743.16284235223191, 738.25118327598705, 741.87640555621192,
        752.16133105273627, 753.40349005967096, 752.53146661644837,
        751.26256717036415, 736.76599837326251, 730.34207449912219,
        722.61602457644301, 720.72503890045414, 718.75758033015086,
        717.38696724627926, 705.60076764380165, 700.77815285945371,
        695.62965212980089, 697.5250493421853]

        self.bb_bandwidth_period_6_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, 0.029762744070567292, 0.015924315510963259,
        0.016411246830892286, 0.011767311600503474, 0.011808549519979793,
        0.011427611985725204, 0.013003740094889849, 0.01262915996286966,
        0.017092418619119462, 0.018458852627534054, 0.037544133410631376,
        0.048455691370547747, 0.066115809985329774, 0.065146656731671457,
        0.07448224980492732, 0.061143891756178639, 0.047517980908341001,
        0.044494244286115335, 0.049330883794422242, 0.049785416758294947,
        0.040934080514761759, 0.023478174531485943, 0.01790102241129678,
        0.018629836257193041, 0.018984609284321868, 0.019073596677803752,
        0.022642444906910295, 0.056319998952028466, 0.052773997163851061,
        0.054185043869097921, 0.079431501944306218, 0.10285804507410032,
        0.10599853177595028, 0.075756853365512147, 0.065561459446232859,
        0.059877000313716996, 0.059798332106171588, 0.057441671708845995,
        0.07350269988434073, 0.069654217816925879, 0.056151339033763625,
        0.037336203793465424, 0.039992035650287784, 0.029653650446448417,
        0.028486423122266347, 0.02328959651737332, 0.023766437149837644,
        0.041877764958299951, 0.042271124906660101, 0.045871116272230679,
        0.043072140873862054, 0.029160775209502447, 0.018232656546951029,
        0.023341471576031551, 0.024267599842649864, 0.02628512556858997,
        0.024483281954310685, 0.023772008042750856, 0.0067236009469093493,
        0.0060610656405819053, 0.01567282927047153, 0.019353460320035983,
        0.019424672673156413, 0.023199618101178578, 0.02608651123758839,
        0.023788894936098284, 0.030234893348296522, 0.037478493882592577,
        0.039964912893803189, 0.033270696237166636, 0.022971423254643155,
        0.023274877798400279, 0.022611548140712961, 0.026141697538999947,
        0.030281531715110312, 0.037731237161319667, 0.040518664625930033,
        0.03404993178124021, 0.038194038822056658, 0.036622033284523597,
        0.03817847021662945, 0.030452503590707322, 0.012426685577900175,
        0.0094859522872056453, 0.0095453665843518703, 0.0096508312663897283,
        0.01022700258046453, 0.014000922693908886, 0.018792354745071755,
        0.019886932723972822, 0.015580761337465034, 0.015722266244403333,
        0.013306857891008633, 0.012010852915034381, 0.012087894275387027,
        0.012240197379036342, 0.0057512977692673432, 0.005241533122443724,
        0.019259713067351483, 0.021658278613777483, 0.020117526499630119,
        0.017082528814957587, 0.02323028976640993, 0.062000056676565267,
        0.083055441861107582, 0.093582512467926995, 0.088777285565028993,
        0.061973862183354496, 0.019181557445934274, 0.012088655950524234,
        0.010645224669307044, 0.012050804638609336, 0.04095448924794113,
        0.047879200274980896, 0.057744860700327943, 0.052107650893023313,
        0.045889736336821522, 0.033838021433548277, 0.053528547682287292,
        0.054834882884566158, 0.058080210682613688, 0.042653058775305272]

        self.bb_range_period_6_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, 23.945665346548367, 12.864352123428262, 13.291414104183559,
        9.5458589043744269, 9.5791347324393428, 9.2850680605415619,
        10.583483988428952, 10.285229970960927, 13.899326922153023,
        15.001109588589998, 30.419508360407235, 39.065139901906832,
        52.843171323791466, 51.665533320903023, 58.530013952957006,
        47.588596673292614, 36.83071182224603, 34.471989917741666,
        38.29819607007903, 38.667503439221719, 31.892015022920987,
        18.372884609905213, 14.035087776315777, 14.564681786965139,
        14.843211691993474, 14.912087565312731, 17.687787374972004,
        43.697654653564769, 40.831593432319323, 41.962342906732601,
        61.771098959518895, 80.537677862945429, 83.471370474486093,
        60.008771210734039, 52.046838734184576, 47.615288394473509,
        47.551633690827657, 45.65770423001527, 58.638616400229921,
        55.989221184875305, 45.50888216112935, 30.509527837855558,
        32.881451711666614, 24.451214012123501, 23.498592865673118,
        19.249511393510375, 19.641217432283156, 34.457373989063854,
        34.561646694308592, 37.352314817454271, 35.002359920439631,
        23.612208706514366, 14.741193981492643, 18.847849273119209,
        19.589534620982249, 21.205656478087803, 19.715366821058296,
        19.106196784173335, 5.3926081094607525, 4.863176830929433,
        12.593536260937753, 15.58166443826417, 15.638544973522585,
        18.734078277003391, 21.116987369309072, 19.266546712429545,
        24.435336889204109, 30.193674098320116, 32.165626926201185,
        26.70167452094006, 18.338316898414178, 18.517298819092275,
        17.985941423480881, 20.76382752127688, 24.076593520586584,
        30.042302767190677, 32.380288242488859, 27.257083890655394,
        30.52722209584249, 29.279132500810192, 30.4540112300499,
        24.229432973600979, 9.8565984666788609, 7.5152615094591511,
        7.5658325531446735, 7.6602668941029606, 8.1261717103855062,
        11.133790409779067, 14.973873543238142, 15.892841155690121,
        12.471230893540451, 12.609047897794881, 10.694322481266909,
        9.669877627629603, 9.7434673271661723, 9.8704339654680098,
        4.6416903051463123, 4.2311227824302478, 15.515560648014798,
        17.414338919407783, 16.147433232560616, 13.692757209561478,
        18.566809095803137, 49.128948243938112, 65.324904558334765,
        72.960981962202823, 68.584300114692724, 47.447188887576203,
        14.567337894527554, 9.163019880658112, 8.0537334337698212,
        9.1081989926049118, 30.804669920141805, 35.825851001755836,
        42.967950847114025, 38.559922199091716, 33.758172673031595,
        24.69273217410796, 38.808464712396699, 39.510360947759409,
        41.610695740398342, 30.39990131562945]

        self.bb_percent_bandwidth_period_6_expected = [np.nan, np.nan, np.nan,
        np.nan, np.nan, 0.71416541403692657, 0.83866195707846203,
        0.89900444691314974, 0.63426415365090116, 0.35767677651338675,
        0.83799788142320564, 0.87889224421599332, 0.59106910290885928,
        0.1196458507468704, 0.28479369714165292, 0.0048133863682257843,
        0.12285215487954285, 0.063393602452485501, 0.21267111658762514,
        0.1349736048726756, 0.20633721149749989, 0.52144949040932731,
        0.9260947328072221, 0.74639976904914895, 0.59094630772307843,
        0.49665538014484123, 0.633257971478976, 0.55426874977952445,
        0.10017435200369072, 0.79003157061501017, 0.37672193277556709,
        0.15974639983239608, -0.018601440885751042, 0.45207959077301557,
        0.63972845478064588, 0.95207225499258885, 0.85985227580047796,
        0.67435119671099153, 0.3163046316242244, 0.27571484422038112,
        0.35722372871057828, 0.71618605297219873, 0.8295537285638418,
        0.87151285854545757, 0.74171319134171387, 0.75559113110015375,
        0.87343525582840109, 0.91178230568195906, 0.47955111759473479,
        0.36062995266478265, 0.52917822978385209, 0.24865780679396729,
        0.036577182625657373, 0.12333006154254761, 0.22670145389320973,
        0.4750016855438069, 0.49343559927296865, 0.88429722905161479,
        0.14063096880802617, 0.28815219042748808, 0.23945630941870744,
        0.37480155171666485, 0.32483867906988173, 0.87427776919156563,
        0.55689011037128311, 1.0187846525362536, 0.86068033824415258,
        0.34418840302649006, 0.89731516134797906, 0.80552022188749373,
        0.24740327162381351, 0.15609914152458346, 0.16096651128534847,
        0.28621070615399286, 0.45025280784200755, 0.0719345432034246,
        0.12890555832140957, 0.68838787770707444, 0.22066807075637879,
        0.82182016640801603, 0.89183636347352613, 0.774086503910557,
        0.36670131889717433, 0.24230650132629816, 0.17058450247004101,
        0.31102653583047624, 0.50715383366677447, 0.50405819514057526,
        0.37336878890123959, 0.62974998584373221, 0.87183212709286495,
        0.79165024866150302, 0.89803755087524306, 0.89691355187229727,
        0.89388803667484718, 0.561341178471503, 0.81511763342799493,
        0.81605555245978223, 0.82110023720757952, 0.75025314412816568,
        0.60992424485043439, 0.10395174764351146, 0.42909683423846284,
        -0.03795456419646949, 0.20541517402749962, 0.34300910469854978,
        0.4543554310914491, 0.073970952187581138, -0.040652051714621898,
        0.12416069594495738, 0.19856034359944733, 0.28095083994135567,
        0.36679927413666208, 0.15436375290700455, 0.4012334348515052,
        0.10908399076977786, 0.21271305460156581, -0.036877472675652036,
        0.1523460112813585, 0.15974639907730281, 0.30562720118308356,
        0.25008520904313003, 0.015916940699370632, 0.042754393107139112,
        0.2073341509427761, 0.22254729716543903, 0.41858526202755941]

        self.percent_b_period_6_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, 71.416541403692662, 83.866195707846202, 89.900444691314974,
        63.426415365090115, 35.767677651338673, 83.799788142320565,
        87.889224421599337, 59.106910290885928, 11.96458507468704,
        28.479369714165294, 0.48133863682257844, 12.285215487954284,
        6.3393602452485505, 21.267111658762513, 13.49736048726756,
        20.633721149749988, 52.14494904093273, 92.609473280722213,
        74.639976904914889, 59.094630772307845, 49.66553801448412,
        63.325797147897603, 55.426874977952444, 10.017435200369071,
        79.003157061501014, 37.672193277556708, 15.974639983239609,
        -1.8601440885751042, 45.20795907730156, 63.972845478064585,
        95.207225499258882, 85.985227580047791, 67.435119671099159,
        31.630463162422441, 27.571484422038111, 35.722372871057829,
        71.618605297219872, 82.955372856384173, 87.151285854545762,
        74.171319134171384, 75.559113110015375, 87.343525582840115,
        91.1782305681959, 47.955111759473482, 36.062995266478268,
        52.91782297838521, 24.865780679396728, 3.6577182625657372,
        12.333006154254761, 22.670145389320972, 47.500168554380693,
        49.343559927296866, 88.429722905161483, 14.063096880802616,
        28.815219042748808, 23.945630941870743, 37.480155171666482,
        32.483867906988174, 87.427776919156557, 55.68901103712831,
        101.87846525362536, 86.068033824415252, 34.418840302649009,
        89.7315161347979, 80.552022188749376, 24.740327162381352,
        15.609914152458346, 16.096651128534848, 28.621070615399287,
        45.025280784200753, 7.1934543203424601, 12.890555832140956,
        68.838787770707441, 22.066807075637879, 82.182016640801606,
        89.183636347352618, 77.408650391055701, 36.670131889717432,
        24.230650132629815, 17.0584502470041, 31.102653583047623,
        50.715383366677443, 50.405819514057526, 37.336878890123955,
        62.974998584373218, 87.183212709286494, 79.165024866150304,
        89.803755087524308, 89.691355187229732, 89.388803667484723,
        56.1341178471503, 81.511763342799497, 81.605555245978223,
        82.110023720757951, 75.02531441281657, 60.992424485043436,
        10.395174764351147, 42.909683423846282, -3.7954564196469489,
        20.54151740274996, 34.300910469854976, 45.435543109144909,
        7.397095218758114, -4.06520517146219, 12.416069594495738,
        19.856034359944733, 28.095083994135567, 36.679927413666206,
        15.436375290700454, 40.123343485150521, 10.908399076977785,
        21.271305460156579, -3.6877472675652037, 15.23460112813585,
        15.974639907730282, 30.562720118308356, 25.008520904313002,
        1.5916940699370632, 4.275439310713911, 20.733415094277611,
        22.254729716543903, 41.858526202755939]

    def test_upper_bollinger_bands_period_6(self):
        period = 6
        upper_bb = bollinger_bands.upper_bollinger_band(self.data, period)
        np.testing.assert_array_equal(upper_bb, self.upper_bb_period_6_expected)

    def test_upper_bollinger_bands_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            bollinger_bands.upper_bollinger_band(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)

    def test_middle_bollinger_bands_period_6(self):
        period = 6
        middle_bb = bollinger_bands.middle_bollinger_band(self.data, period)
        np.testing.assert_array_equal(middle_bb, self.middle_bb_period_6_expected)

    def test_middle_bollinger_bands_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            bollinger_bands.middle_bollinger_band(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)

    def test_lower_bollinger_bands_period_6(self):
        period = 6
        lower_bb = bollinger_bands.lower_bollinger_band(self.data, period)
        np.testing.assert_array_equal(lower_bb, self.lower_bb_period_6_expected)

    def test_lower_bollinger_bands_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            bollinger_bands.lower_bollinger_band(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)

    def test_bandwidth_period_6(self):
        period = 6
        bb_bandwidth = bollinger_bands.bandwidth(self.data, period)
        np.testing.assert_array_equal(bb_bandwidth, self.bb_bandwidth_period_6_expected)

    def test_bandwidth_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            bollinger_bands.bandwidth(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)

    def test_range_period_6(self):
        period = 6
        bb_range = bollinger_bands.bb_range(self.data, period)
        np.testing.assert_array_equal(bb_range, self.bb_range_period_6_expected)

    def test_range_period_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            bollinger_bands.bb_range(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)

    def test_percent_bandwidth_period_6(self):
        period = 6
        bb_percent_bandwidth = bollinger_bands.percent_bandwidth(self.data, period)
        np.testing.assert_array_equal(bb_percent_bandwidth, self.bb_percent_bandwidth_period_6_expected)

    def test_percent_bandwidth_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            bollinger_bands.percent_bandwidth(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)

    def test_percent_b_period_6(self):
        period = 6
        percent_b = bollinger_bands.percent_b(self.data, period)
        np.testing.assert_array_equal(percent_b, self.percent_b_period_6_expected)

    def test_percent_b_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            bollinger_bands.percent_b(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)
