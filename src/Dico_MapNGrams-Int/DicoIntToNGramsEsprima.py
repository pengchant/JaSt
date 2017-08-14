#!/usr/bin/python
 
'''
	Configuration file storing the dictionary dicoIntToNGrams.
		Key: Integer;
		Value: Unique n-gram.
'''


dicoIntToNGrams = { 
	'0' : (0, 2, 6, 0), 
	'1' : (0, 2, 6, 2), 
	'10' : (0, 3, 3, 2), 
	'100' : (2, 3, 3, 4), 
	'1000' : (7, 11, 6, 6), 
	'1001' : (7, 11, 11, 10), 
	'1002' : (8, 2, 6, 2), 
	'1003' : (8, 2, 6, 6), 
	'1004' : (8, 2, 6, 7), 
	'1005' : (8, 3, 2, 6), 
	'1006' : (8, 3, 6, 2), 
	'1007' : (8, 3, 6, 3), 
	'1008' : (8, 3, 6, 6), 
	'1009' : (8, 6, 2, 6), 
	'101' : (2, 3, 3, 5), 
	'1010' : (8, 6, 3, 2), 
	'1011' : (8, 6, 3, 3), 
	'1012' : (8, 6, 3, 6), 
	'1013' : (8, 6, 3, 8), 
	'1014' : (8, 6, 4, 6), 
	'1015' : (8, 6, 5, 6), 
	'1016' : (8, 6, 6, 2), 
	'1017' : (8, 6, 6, 3), 
	'1018' : (8, 6, 6, 4), 
	'1019' : (8, 6, 6, 5), 
	'102' : (2, 3, 3, 6), 
	'1020' : (8, 6, 6, 6), 
	'1021' : (8, 6, 6, 7), 
	'1022' : (8, 6, 6, 8), 
	'1023' : (8, 6, 6, 10), 
	'1024' : (8, 6, 6, 11), 
	'1025' : (8, 6, 7, 3), 
	'1026' : (8, 6, 7, 6), 
	'1027' : (8, 6, 8, 3), 
	'1028' : (8, 6, 8, 6), 
	'1029' : (8, 6, 10, 2), 
	'103' : (2, 3, 3, 7), 
	'1030' : (8, 6, 10, 3), 
	'1031' : (8, 6, 10, 6), 
	'1032' : (8, 6, 10, 8), 
	'1033' : (8, 6, 10, 10), 
	'1034' : (8, 6, 10, 11), 
	'1035' : (8, 6, 11, 2), 
	'1036' : (8, 6, 11, 3), 
	'1037' : (8, 6, 11, 10), 
	'1038' : (8, 10, 2, 6), 
	'1039' : (8, 10, 3, 2), 
	'104' : (2, 3, 4, 6), 
	'1040' : (8, 10, 6, 6), 
	'1041' : (8, 10, 10, 10), 
	'1042' : (8, 11, 2, 6), 
	'1043' : (8, 11, 6, 6), 
	'1044' : (9, 2, 6, 2), 
	'1045' : (9, 2, 6, 5), 
	'1046' : (9, 2, 6, 7), 
	'1047' : (9, 2, 9, 2), 
	'1048' : (9, 2, 9, 3), 
	'1049' : (9, 2, 9, 6), 
	'105' : (2, 3, 6, 2), 
	'1050' : (9, 3, 2, 6), 
	'1051' : (9, 3, 2, 9), 
	'1052' : (9, 3, 6, 2), 
	'1053' : (9, 3, 7, 6), 
	'1054' : (9, 6, 0, 6), 
	'1055' : (9, 6, 2, 6), 
	'1056' : (9, 6, 3, 2), 
	'1057' : (9, 6, 3, 6), 
	'1058' : (9, 6, 3, 9), 
	'1059' : (9, 6, 6, 2), 
	'106' : (2, 3, 6, 3), 
	'1060' : (9, 6, 6, 3), 
	'1061' : (9, 6, 6, 5), 
	'1062' : (9, 6, 6, 6), 
	'1063' : (9, 6, 6, 7), 
	'1064' : (9, 6, 6, 10), 
	'1065' : (9, 6, 7, 6), 
	'1066' : (9, 6, 7, 9), 
	'1067' : (9, 6, 9, 2), 
	'1068' : (9, 6, 9, 3), 
	'1069' : (9, 6, 10, 2), 
	'107' : (2, 3, 6, 5), 
	'1070' : (9, 6, 10, 6), 
	'1071' : (9, 7, 6, 2), 
	'1072' : (9, 9, 7, 6), 
	'1073' : (10, 0, 6, 6), 
	'1074' : (10, 0, 6, 10), 
	'1075' : (10, 0, 10, 6), 
	'1076' : (10, 2, 2, 6), 
	'1077' : (10, 2, 3, 2), 
	'1078' : (10, 2, 6, 0), 
	'1079' : (10, 2, 6, 2), 
	'108' : (2, 3, 6, 6), 
	'1080' : (10, 2, 6, 3), 
	'1081' : (10, 2, 6, 4), 
	'1082' : (10, 2, 6, 5), 
	'1083' : (10, 2, 6, 6), 
	'1084' : (10, 2, 6, 7), 
	'1085' : (10, 2, 6, 8), 
	'1086' : (10, 2, 6, 9), 
	'1087' : (10, 2, 6, 10), 
	'1088' : (10, 3, 0, 3), 
	'1089' : (10, 3, 0, 6), 
	'109' : (2, 3, 6, 10), 
	'1090' : (10, 3, 2, 2), 
	'1091' : (10, 3, 2, 3), 
	'1092' : (10, 3, 2, 6), 
	'1093' : (10, 3, 3, 2), 
	'1094' : (10, 3, 3, 6), 
	'1095' : (10, 3, 3, 7), 
	'1096' : (10, 3, 4, 6), 
	'1097' : (10, 3, 5, 6), 
	'1098' : (10, 3, 6, 0), 
	'1099' : (10, 3, 6, 2), 
	'11' : (0, 3, 3, 4), 
	'110' : (2, 3, 7, 6), 
	'1100' : (10, 3, 6, 3), 
	'1101' : (10, 3, 6, 4), 
	'1102' : (10, 3, 6, 5), 
	'1103' : (10, 3, 6, 6), 
	'1104' : (10, 3, 6, 7), 
	'1105' : (10, 3, 6, 8), 
	'1106' : (10, 3, 6, 10), 
	'1107' : (10, 3, 7, 3), 
	'1108' : (10, 3, 7, 6), 
	'1109' : (10, 3, 8, 6), 
	'111' : (2, 5, 6, 2), 
	'1110' : (10, 3, 9, 2), 
	'1111' : (10, 3, 10, 10), 
	'1112' : (10, 3, 11, 2), 
	'1113' : (10, 5, 3, 5), 
	'1114' : (10, 5, 6, 2), 
	'1115' : (10, 5, 6, 5), 
	'1116' : (10, 5, 6, 6), 
	'1117' : (10, 5, 6, 7), 
	'1118' : (10, 5, 6, 10), 
	'1119' : (10, 5, 10, 6), 
	'112' : (2, 5, 6, 6), 
	'1120' : (10, 6, 0, 6), 
	'1121' : (10, 6, 2, 6), 
	'1122' : (10, 6, 2, 10), 
	'1123' : (10, 6, 3, 0), 
	'1124' : (10, 6, 3, 2), 
	'1125' : (10, 6, 3, 3), 
	'1126' : (10, 6, 3, 5), 
	'1127' : (10, 6, 3, 6), 
	'1128' : (10, 6, 4, 6), 
	'1129' : (10, 6, 5, 6), 
	'113' : (2, 6, 0, 2), 
	'1130' : (10, 6, 6, 2), 
	'1131' : (10, 6, 6, 3), 
	'1132' : (10, 6, 6, 5), 
	'1133' : (10, 6, 6, 6), 
	'1134' : (10, 6, 6, 7), 
	'1135' : (10, 6, 6, 8), 
	'1136' : (10, 6, 6, 10), 
	'1137' : (10, 6, 6, 11), 
	'1138' : (10, 6, 7, 6), 
	'1139' : (10, 6, 8, 6), 
	'114' : (2, 6, 0, 3), 
	'1140' : (10, 6, 9, 7), 
	'1141' : (10, 6, 10, 2), 
	'1142' : (10, 6, 10, 3), 
	'1143' : (10, 6, 10, 6), 
	'1144' : (10, 6, 10, 10), 
	'1145' : (10, 6, 10, 11), 
	'1146' : (10, 6, 11, 2), 
	'1147' : (10, 6, 11, 3), 
	'1148' : (10, 6, 11, 11), 
	'1149' : (10, 7, 3, 2), 
	'115' : (2, 6, 0, 6), 
	'1150' : (10, 7, 6, 0), 
	'1151' : (10, 7, 6, 2), 
	'1152' : (10, 7, 6, 3), 
	'1153' : (10, 7, 6, 4), 
	'1154' : (10, 7, 6, 5), 
	'1155' : (10, 7, 6, 6), 
	'1156' : (10, 7, 6, 7), 
	'1157' : (10, 7, 6, 10), 
	'1158' : (10, 7, 6, 11), 
	'1159' : (10, 7, 10, 6), 
	'116' : (2, 6, 0, 10), 
	'1160' : (10, 8, 6, 2), 
	'1161' : (10, 8, 6, 4), 
	'1162' : (10, 8, 6, 6), 
	'1163' : (10, 8, 6, 10), 
	'1164' : (10, 8, 10, 6), 
	'1165' : (10, 10, 2, 3), 
	'1166' : (10, 10, 2, 6), 
	'1167' : (10, 10, 3, 0), 
	'1168' : (10, 10, 3, 2), 
	'1169' : (10, 10, 3, 3), 
	'117' : (2, 6, 0, 11), 
	'1170' : (10, 10, 3, 4), 
	'1171' : (10, 10, 3, 5), 
	'1172' : (10, 10, 3, 6), 
	'1173' : (10, 10, 3, 7), 
	'1174' : (10, 10, 3, 8), 
	'1175' : (10, 10, 3, 9), 
	'1176' : (10, 10, 5, 3), 
	'1177' : (10, 10, 5, 6), 
	'1178' : (10, 10, 6, 2), 
	'1179' : (10, 10, 6, 3), 
	'118' : (2, 6, 2, 2), 
	'1180' : (10, 10, 6, 4), 
	'1181' : (10, 10, 6, 5), 
	'1182' : (10, 10, 6, 6), 
	'1183' : (10, 10, 6, 7), 
	'1184' : (10, 10, 6, 8), 
	'1185' : (10, 10, 6, 10), 
	'1186' : (10, 10, 6, 11), 
	'1187' : (10, 10, 7, 3), 
	'1188' : (10, 10, 7, 6), 
	'1189' : (10, 10, 7, 10), 
	'119' : (2, 6, 2, 3), 
	'1190' : (10, 10, 8, 6), 
	'1191' : (10, 10, 10, 2), 
	'1192' : (10, 10, 10, 3), 
	'1193' : (10, 10, 10, 5), 
	'1194' : (10, 10, 10, 6), 
	'1195' : (10, 10, 10, 7), 
	'1196' : (10, 10, 10, 8), 
	'1197' : (10, 10, 10, 10), 
	'1198' : (10, 10, 10, 11), 
	'1199' : (10, 10, 11, 2), 
	'12' : (0, 3, 3, 6), 
	'120' : (2, 6, 2, 5), 
	'1200' : (10, 10, 11, 3), 
	'1201' : (10, 10, 11, 6), 
	'1202' : (10, 10, 11, 10), 
	'1203' : (10, 10, 11, 11), 
	'1204' : (10, 11, 2, 6), 
	'1205' : (10, 11, 3, 2), 
	'1206' : (10, 11, 3, 3), 
	'1207' : (10, 11, 3, 6), 
	'1208' : (10, 11, 3, 7), 
	'1209' : (10, 11, 6, 2), 
	'121' : (2, 6, 2, 6), 
	'1210' : (10, 11, 6, 3), 
	'1211' : (10, 11, 6, 6), 
	'1212' : (10, 11, 6, 11), 
	'1213' : (10, 11, 7, 6), 
	'1214' : (10, 11, 10, 2), 
	'1215' : (10, 11, 10, 3), 
	'1216' : (10, 11, 10, 6), 
	'1217' : (10, 11, 10, 7), 
	'1218' : (10, 11, 10, 10), 
	'1219' : (10, 11, 10, 11), 
	'122' : (2, 6, 2, 9), 
	'1220' : (10, 11, 11, 2), 
	'1221' : (10, 11, 11, 3), 
	'1222' : (10, 11, 11, 10), 
	'1223' : (10, 11, 11, 11), 
	'1224' : (11, 0, 6, 0), 
	'1225' : (11, 0, 6, 2), 
	'1226' : (11, 0, 6, 6), 
	'1227' : (11, 2, 3, 2), 
	'1228' : (11, 2, 6, 0), 
	'1229' : (11, 2, 6, 2), 
	'123' : (2, 6, 2, 10), 
	'1230' : (11, 2, 6, 3), 
	'1231' : (11, 2, 6, 4), 
	'1232' : (11, 2, 6, 5), 
	'1233' : (11, 2, 6, 6), 
	'1234' : (11, 2, 6, 7), 
	'1235' : (11, 2, 6, 8), 
	'1236' : (11, 2, 6, 10), 
	'1237' : (11, 2, 6, 11), 
	'1238' : (11, 2, 11, 6), 
	'1239' : (11, 3, 0, 6), 
	'124' : (2, 6, 2, 11), 
	'1240' : (11, 3, 2, 6), 
	'1241' : (11, 3, 3, 2), 
	'1242' : (11, 3, 3, 6), 
	'1243' : (11, 3, 6, 0), 
	'1244' : (11, 3, 6, 2), 
	'1245' : (11, 3, 6, 3), 
	'1246' : (11, 3, 6, 5), 
	'1247' : (11, 3, 6, 6), 
	'1248' : (11, 3, 6, 7), 
	'1249' : (11, 3, 6, 8), 
	'125' : (2, 6, 3, 0), 
	'1250' : (11, 3, 6, 11), 
	'1251' : (11, 3, 7, 6), 
	'1252' : (11, 3, 10, 2), 
	'1253' : (11, 3, 11, 2), 
	'1254' : (11, 5, 6, 6), 
	'1255' : (11, 5, 11, 6), 
	'1256' : (11, 6, 0, 6), 
	'1257' : (11, 6, 0, 11), 
	'1258' : (11, 6, 2, 6), 
	'1259' : (11, 6, 2, 11), 
	'126' : (2, 6, 3, 2), 
	'1260' : (11, 6, 3, 0), 
	'1261' : (11, 6, 3, 2), 
	'1262' : (11, 6, 3, 3), 
	'1263' : (11, 6, 3, 5), 
	'1264' : (11, 6, 3, 6), 
	'1265' : (11, 6, 3, 7), 
	'1266' : (11, 6, 3, 11), 
	'1267' : (11, 6, 4, 6), 
	'1268' : (11, 6, 5, 6), 
	'1269' : (11, 6, 6, 2), 
	'127' : (2, 6, 3, 3), 
	'1270' : (11, 6, 6, 3), 
	'1271' : (11, 6, 6, 5), 
	'1272' : (11, 6, 6, 6), 
	'1273' : (11, 6, 6, 7), 
	'1274' : (11, 6, 6, 10), 
	'1275' : (11, 6, 6, 11), 
	'1276' : (11, 6, 7, 6), 
	'1277' : (11, 6, 8, 6), 
	'1278' : (11, 6, 10, 2), 
	'1279' : (11, 6, 10, 3), 
	'128' : (2, 6, 3, 4), 
	'1280' : (11, 6, 10, 10), 
	'1281' : (11, 6, 11, 3), 
	'1282' : (11, 6, 11, 6), 
	'1283' : (11, 7, 6, 2), 
	'1284' : (11, 7, 6, 3), 
	'1285' : (11, 7, 6, 6), 
	'1286' : (11, 7, 6, 7), 
	'1287' : (11, 7, 6, 10), 
	'1288' : (11, 7, 6, 11), 
	'1289' : (11, 7, 11, 2), 
	'129' : (2, 6, 3, 5), 
	'1290' : (11, 7, 11, 3), 
	'1291' : (11, 7, 11, 6), 
	'1292' : (11, 8, 6, 2), 
	'1293' : (11, 8, 6, 6), 
	'1294' : (11, 10, 2, 6), 
	'1295' : (11, 10, 3, 2), 
	'1296' : (11, 10, 3, 6), 
	'1297' : (11, 10, 6, 3), 
	'1298' : (11, 10, 6, 10), 
	'1299' : (11, 10, 7, 6), 
	'13' : (0, 3, 3, 7), 
	'130' : (2, 6, 3, 6), 
	'1300' : (11, 10, 10, 2), 
	'1301' : (11, 10, 10, 3), 
	'1302' : (11, 10, 10, 6), 
	'1303' : (11, 10, 10, 7), 
	'1304' : (11, 10, 10, 10), 
	'1305' : (11, 10, 10, 11), 
	'1306' : (11, 10, 11, 2), 
	'1307' : (11, 10, 11, 3), 
	'1308' : (11, 10, 11, 10), 
	'1309' : (11, 10, 11, 11), 
	'131' : (2, 6, 3, 7), 
	'1310' : (11, 11, 2, 6), 
	'1311' : (11, 11, 3, 2), 
	'1312' : (11, 11, 3, 6), 
	'1313' : (11, 11, 6, 3), 
	'1314' : (11, 11, 6, 6), 
	'1315' : (11, 11, 7, 6), 
	'1316' : (11, 11, 10, 2), 
	'1317' : (11, 11, 10, 3), 
	'1318' : (11, 11, 10, 10), 
	'1319' : (11, 11, 11, 2), 
	'132' : (2, 6, 3, 8), 
	'1320' : (11, 11, 11, 3), 
	'1321' : (11, 11, 11, 6), 
	'1322' : (11, 11, 11, 7), 
	'1323' : (11, 11, 11, 10), 
	'1324' : (11, 11, 11, 11), 
	'1325' : (4, 6, 11, 0), 
	'1326' : (6, 6, 11, 4), 
	'1327' : (6, 11, 4, 6), 
	'1328' : (11, 3, 6, 10), 
	'1329' : (11, 4, 6, 11), 
	'133' : (2, 6, 3, 9), 
	'1330' : (11, 11, 10, 11), 
	'1331' : (2, 11, 6, 3), 
	'1332' : (3, 2, 11, 6), 
	'1333' : (10, 3, 10, 2), 
	'1334' : (10, 6, 11, 10), 
	'1335' : (10, 10, 3, 10), 
	'1336' : (0, 10, 6, 10), 
	'1337' : (3, 7, 3, 0), 
	'1338' : (7, 6, 0, 3), 
	'1339' : (3, 3, 3, 3), 
	'134' : (2, 6, 3, 10), 
	'1340' : (10, 3, 6, 11), 
	'1341' : (11, 0, 6, 3), 
	'1342' : (0, 6, 3, 11), 
	'1343' : (0, 6, 11, 7), 
	'1344' : (3, 7, 6, 8), 
	'1345' : (3, 10, 6, 10), 
	'1346' : (4, 6, 3, 11), 
	'1347' : (4, 6, 7, 3), 
	'1348' : (4, 6, 11, 7), 
	'1349' : (5, 6, 3, 8), 
	'135' : (2, 6, 3, 11), 
	'1350' : (5, 6, 3, 11), 
	'1351' : (5, 6, 11, 7), 
	'1352' : (7, 6, 3, 11), 
	'1353' : (8, 6, 3, 11), 
	'1354' : (11, 6, 5, 11), 
	'1355' : (11, 7, 6, 0), 
	'1356' : (11, 7, 6, 4), 
	'1357' : (11, 7, 6, 5), 
	'1358' : (0, 6, 10, 11), 
	'1359' : (0, 6, 11, 0), 
	'136' : (2, 6, 4, 2), 
	'1360' : (2, 3, 2, 11), 
	'1361' : (2, 6, 10, 0), 
	'1362' : (3, 5, 6, 8), 
	'1363' : (4, 11, 6, 2), 
	'1364' : (5, 6, 10, 7), 
	'1365' : (5, 10, 6, 5), 
	'1366' : (6, 4, 11, 6), 
	'1367' : (6, 6, 4, 11), 
	'1368' : (6, 6, 10, 0), 
	'1369' : (6, 8, 6, 0), 
	'137' : (2, 6, 4, 3), 
	'1370' : (6, 10, 2, 10), 
	'1371' : (6, 10, 3, 9), 
	'1372' : (6, 11, 6, 0), 
	'1373' : (7, 2, 6, 4), 
	'1374' : (7, 3, 2, 10), 
	'1375' : (7, 3, 6, 0), 
	'1376' : (8, 6, 0, 6), 
	'1377' : (8, 6, 10, 7), 
	'1378' : (8, 6, 11, 11), 
	'1379' : (8, 10, 6, 8), 
	'138' : (2, 6, 4, 6), 
	'1380' : (9, 6, 6, 11), 
	'1381' : (10, 2, 10, 6), 
	'1382' : (10, 3, 3, 3), 
	'1383' : (10, 3, 3, 5), 
	'1384' : (10, 6, 5, 10), 
	'1385' : (10, 6, 6, 0), 
	'1386' : (10, 6, 7, 10), 
	'1387' : (10, 7, 6, 8), 
	'1388' : (10, 7, 10, 10), 
	'1389' : (11, 0, 6, 11), 
	'139' : (2, 6, 4, 10), 
	'1390' : (2, 6, 7, 7), 
	'1391' : (5, 10, 6, 10), 
	'1392' : (6, 7, 7, 7), 
	'1393' : (7, 7, 6, 6), 
	'1394' : (7, 7, 6, 7), 
	'1395' : (7, 7, 7, 6), 
	'1396' : (7, 7, 7, 7), 
	'1397' : (0, 6, 6, 9), 
	'14' : (0, 3, 6, 2), 
	'140' : (2, 6, 4, 11), 
	'141' : (2, 6, 5, 2), 
	'142' : (2, 6, 5, 3), 
	'143' : (2, 6, 5, 6), 
	'144' : (2, 6, 5, 9), 
	'145' : (2, 6, 5, 10), 
	'146' : (2, 6, 5, 11), 
	'147' : (2, 6, 6, 0), 
	'148' : (2, 6, 6, 2), 
	'149' : (2, 6, 6, 3), 
	'15' : (0, 3, 6, 3), 
	'150' : (2, 6, 6, 4), 
	'151' : (2, 6, 6, 5), 
	'152' : (2, 6, 6, 6), 
	'153' : (2, 6, 6, 7), 
	'154' : (2, 6, 6, 8), 
	'155' : (2, 6, 6, 9), 
	'156' : (2, 6, 6, 10), 
	'157' : (2, 6, 6, 11), 
	'158' : (2, 6, 7, 2), 
	'159' : (2, 6, 7, 3), 
	'16' : (0, 3, 6, 4), 
	'160' : (2, 6, 7, 6), 
	'161' : (2, 6, 7, 9), 
	'162' : (2, 6, 7, 10), 
	'163' : (2, 6, 7, 11), 
	'164' : (2, 6, 8, 2), 
	'165' : (2, 6, 8, 3), 
	'166' : (2, 6, 8, 6), 
	'167' : (2, 6, 8, 10), 
	'168' : (2, 6, 8, 11), 
	'169' : (2, 6, 9, 2), 
	'17' : (0, 3, 6, 6), 
	'170' : (2, 6, 9, 3), 
	'171' : (2, 6, 9, 6), 
	'172' : (2, 6, 9, 7), 
	'173' : (2, 6, 9, 9), 
	'174' : (2, 6, 10, 2), 
	'175' : (2, 6, 10, 3), 
	'176' : (2, 6, 10, 5), 
	'177' : (2, 6, 10, 6), 
	'178' : (2, 6, 10, 7), 
	'179' : (2, 6, 10, 8), 
	'18' : (0, 3, 6, 7), 
	'180' : (2, 6, 10, 10), 
	'181' : (2, 6, 10, 11), 
	'182' : (2, 6, 11, 0), 
	'183' : (2, 6, 11, 2), 
	'184' : (2, 6, 11, 3), 
	'185' : (2, 6, 11, 5), 
	'186' : (2, 6, 11, 6), 
	'187' : (2, 6, 11, 7), 
	'188' : (2, 6, 11, 8), 
	'189' : (2, 6, 11, 10), 
	'19' : (0, 3, 6, 10), 
	'190' : (2, 6, 11, 11), 
	'191' : (2, 7, 6, 2), 
	'192' : (2, 7, 6, 6), 
	'193' : (2, 9, 2, 6), 
	'194' : (2, 9, 2, 9), 
	'195' : (2, 9, 3, 2), 
	'196' : (2, 9, 3, 6), 
	'197' : (2, 9, 6, 0), 
	'198' : (2, 9, 6, 2), 
	'199' : (2, 9, 6, 3), 
	'2' : (0, 2, 6, 3), 
	'20' : (0, 3, 7, 6), 
	'200' : (2, 9, 6, 6), 
	'201' : (2, 9, 6, 7), 
	'202' : (2, 9, 6, 9), 
	'203' : (2, 9, 6, 10), 
	'204' : (2, 10, 2, 2), 
	'205' : (2, 10, 2, 6), 
	'206' : (2, 10, 3, 2), 
	'207' : (2, 10, 3, 6), 
	'208' : (2, 10, 6, 2), 
	'209' : (2, 10, 6, 3), 
	'21' : (0, 3, 10, 10), 
	'210' : (2, 10, 6, 6), 
	'211' : (2, 10, 6, 7), 
	'212' : (2, 10, 6, 11), 
	'213' : (2, 10, 10, 2), 
	'214' : (2, 10, 10, 3), 
	'215' : (2, 10, 10, 6), 
	'216' : (2, 10, 10, 10), 
	'217' : (2, 11, 2, 6), 
	'218' : (2, 11, 3, 2), 
	'219' : (2, 11, 3, 6), 
	'22' : (0, 6, 0, 3), 
	'220' : (2, 11, 6, 2), 
	'221' : (2, 11, 6, 6), 
	'222' : (2, 11, 6, 7), 
	'223' : (3, 0, 2, 6), 
	'224' : (3, 0, 3, 0), 
	'225' : (3, 0, 3, 2), 
	'226' : (3, 0, 3, 3), 
	'227' : (3, 0, 3, 6), 
	'228' : (3, 0, 3, 7), 
	'229' : (3, 0, 6, 2), 
	'23' : (0, 6, 0, 6), 
	'230' : (3, 0, 6, 3), 
	'231' : (3, 0, 6, 6), 
	'232' : (3, 0, 6, 7), 
	'233' : (3, 0, 6, 10), 
	'234' : (3, 0, 6, 11), 
	'235' : (3, 0, 10, 3), 
	'236' : (3, 0, 10, 6), 
	'237' : (3, 0, 10, 10), 
	'238' : (3, 2, 2, 2), 
	'239' : (3, 2, 2, 3), 
	'24' : (0, 6, 2, 2), 
	'240' : (3, 2, 2, 6), 
	'241' : (3, 2, 2, 7), 
	'242' : (3, 2, 3, 0), 
	'243' : (3, 2, 3, 2), 
	'244' : (3, 2, 3, 3), 
	'245' : (3, 2, 3, 4), 
	'246' : (3, 2, 3, 6), 
	'247' : (3, 2, 3, 7), 
	'248' : (3, 2, 6, 0), 
	'249' : (3, 2, 6, 2), 
	'25' : (0, 6, 2, 3), 
	'250' : (3, 2, 6, 3), 
	'251' : (3, 2, 6, 4), 
	'252' : (3, 2, 6, 5), 
	'253' : (3, 2, 6, 6), 
	'254' : (3, 2, 6, 7), 
	'255' : (3, 2, 6, 8), 
	'256' : (3, 2, 6, 9), 
	'257' : (3, 2, 6, 10), 
	'258' : (3, 2, 6, 11), 
	'259' : (3, 2, 9, 6), 
	'26' : (0, 6, 2, 6), 
	'260' : (3, 2, 10, 2), 
	'261' : (3, 2, 10, 3), 
	'262' : (3, 2, 10, 6), 
	'263' : (3, 2, 10, 10), 
	'264' : (3, 2, 11, 3), 
	'265' : (3, 3, 0, 6), 
	'266' : (3, 3, 2, 3), 
	'267' : (3, 3, 2, 6), 
	'268' : (3, 3, 3, 2), 
	'269' : (3, 3, 3, 6), 
	'27' : (0, 6, 3, 0), 
	'270' : (3, 3, 3, 7), 
	'271' : (3, 3, 4, 6), 
	'272' : (3, 3, 4, 10), 
	'273' : (3, 3, 5, 6), 
	'274' : (3, 3, 5, 10), 
	'275' : (3, 3, 6, 2), 
	'276' : (3, 3, 6, 3), 
	'277' : (3, 3, 6, 4), 
	'278' : (3, 3, 6, 5), 
	'279' : (3, 3, 6, 6), 
	'28' : (0, 6, 3, 2), 
	'280' : (3, 3, 6, 7), 
	'281' : (3, 3, 6, 8), 
	'282' : (3, 3, 6, 10), 
	'283' : (3, 3, 6, 11), 
	'284' : (3, 3, 7, 6), 
	'285' : (3, 3, 11, 2), 
	'286' : (3, 4, 2, 6), 
	'287' : (3, 4, 3, 2), 
	'288' : (3, 4, 3, 3), 
	'289' : (3, 4, 3, 6), 
	'29' : (0, 6, 3, 3), 
	'290' : (3, 4, 3, 7), 
	'291' : (3, 4, 6, 2), 
	'292' : (3, 4, 6, 3), 
	'293' : (3, 4, 6, 4), 
	'294' : (3, 4, 6, 6), 
	'295' : (3, 4, 6, 7), 
	'296' : (3, 4, 6, 8), 
	'297' : (3, 4, 6, 10), 
	'298' : (3, 4, 10, 3), 
	'299' : (3, 4, 10, 10), 
	'3' : (0, 2, 6, 4), 
	'30' : (0, 6, 3, 4), 
	'300' : (3, 5, 2, 6), 
	'301' : (3, 5, 3, 2), 
	'302' : (3, 5, 3, 3), 
	'303' : (3, 5, 3, 6), 
	'304' : (3, 5, 6, 0), 
	'305' : (3, 5, 6, 2), 
	'306' : (3, 5, 6, 3), 
	'307' : (3, 5, 6, 4), 
	'308' : (3, 5, 6, 5), 
	'309' : (3, 5, 6, 6), 
	'31' : (0, 6, 3, 5), 
	'310' : (3, 5, 6, 7), 
	'311' : (3, 5, 6, 10), 
	'312' : (3, 5, 6, 11), 
	'313' : (3, 5, 10, 3), 
	'314' : (3, 5, 11, 6), 
	'315' : (3, 6, 0, 6), 
	'316' : (3, 6, 2, 2), 
	'317' : (3, 6, 2, 3), 
	'318' : (3, 6, 2, 6), 
	'319' : (3, 6, 2, 9), 
	'32' : (0, 6, 3, 6), 
	'320' : (3, 6, 2, 10), 
	'321' : (3, 6, 2, 11), 
	'322' : (3, 6, 3, 0), 
	'323' : (3, 6, 3, 2), 
	'324' : (3, 6, 3, 3), 
	'325' : (3, 6, 3, 4), 
	'326' : (3, 6, 3, 5), 
	'327' : (3, 6, 3, 6), 
	'328' : (3, 6, 3, 7), 
	'329' : (3, 6, 3, 9), 
	'33' : (0, 6, 3, 7), 
	'330' : (3, 6, 3, 11), 
	'331' : (3, 6, 4, 6), 
	'332' : (3, 6, 5, 2), 
	'333' : (3, 6, 5, 3), 
	'334' : (3, 6, 5, 6), 
	'335' : (3, 6, 6, 0), 
	'336' : (3, 6, 6, 2), 
	'337' : (3, 6, 6, 3), 
	'338' : (3, 6, 6, 4), 
	'339' : (3, 6, 6, 5), 
	'34' : (0, 6, 3, 8), 
	'340' : (3, 6, 6, 6), 
	'341' : (3, 6, 6, 7), 
	'342' : (3, 6, 6, 8), 
	'343' : (3, 6, 6, 10), 
	'344' : (3, 6, 6, 11), 
	'345' : (3, 6, 7, 3), 
	'346' : (3, 6, 7, 6), 
	'347' : (3, 6, 8, 6), 
	'348' : (3, 6, 10, 2), 
	'349' : (3, 6, 10, 3), 
	'35' : (0, 6, 3, 10), 
	'350' : (3, 6, 10, 6), 
	'351' : (3, 6, 10, 7), 
	'352' : (3, 6, 10, 10), 
	'353' : (3, 6, 10, 11), 
	'354' : (3, 6, 11, 0), 
	'355' : (3, 6, 11, 2), 
	'356' : (3, 6, 11, 3), 
	'357' : (3, 6, 11, 6), 
	'358' : (3, 6, 11, 10), 
	'359' : (3, 6, 11, 11), 
	'36' : (0, 6, 4, 6), 
	'360' : (3, 7, 2, 6), 
	'361' : (3, 7, 3, 2), 
	'362' : (3, 7, 3, 3), 
	'363' : (3, 7, 3, 6), 
	'364' : (3, 7, 3, 7), 
	'365' : (3, 7, 6, 0), 
	'366' : (3, 7, 6, 2), 
	'367' : (3, 7, 6, 3), 
	'368' : (3, 7, 6, 4), 
	'369' : (3, 7, 6, 5), 
	'37' : (0, 6, 5, 3), 
	'370' : (3, 7, 6, 6), 
	'371' : (3, 7, 6, 7), 
	'372' : (3, 7, 6, 10), 
	'373' : (3, 7, 6, 11), 
	'374' : (3, 8, 6, 2), 
	'375' : (3, 8, 6, 3), 
	'376' : (3, 8, 6, 6), 
	'377' : (3, 9, 2, 6), 
	'378' : (3, 9, 2, 9), 
	'379' : (3, 9, 3, 6), 
	'38' : (0, 6, 5, 6), 
	'380' : (3, 10, 2, 6), 
	'381' : (3, 10, 3, 2), 
	'382' : (3, 10, 3, 5), 
	'383' : (3, 10, 3, 6), 
	'384' : (3, 10, 3, 7), 
	'385' : (3, 10, 5, 6), 
	'386' : (3, 10, 6, 2), 
	'387' : (3, 10, 6, 3), 
	'388' : (3, 10, 6, 6), 
	'389' : (3, 10, 10, 2), 
	'39' : (0, 6, 6, 0), 
	'390' : (3, 10, 10, 3), 
	'391' : (3, 10, 10, 10), 
	'392' : (3, 11, 2, 6), 
	'393' : (3, 11, 5, 6), 
	'394' : (3, 11, 6, 2), 
	'395' : (3, 11, 6, 6), 
	'396' : (3, 11, 10, 2), 
	'397' : (4, 2, 6, 0), 
	'398' : (4, 2, 6, 2), 
	'399' : (4, 2, 6, 3), 
	'4' : (0, 2, 6, 6), 
	'40' : (0, 6, 6, 2), 
	'400' : (4, 2, 6, 4), 
	'401' : (4, 2, 6, 6), 
	'402' : (4, 2, 6, 7), 
	'403' : (4, 3, 2, 2), 
	'404' : (4, 3, 2, 3), 
	'405' : (4, 3, 2, 6), 
	'406' : (4, 3, 3, 6), 
	'407' : (4, 3, 6, 2), 
	'408' : (4, 3, 6, 3), 
	'409' : (4, 3, 6, 6), 
	'41' : (0, 6, 6, 3), 
	'410' : (4, 3, 7, 6), 
	'411' : (4, 6, 0, 6), 
	'412' : (4, 6, 2, 2), 
	'413' : (4, 6, 2, 3), 
	'414' : (4, 6, 2, 6), 
	'415' : (4, 6, 3, 0), 
	'416' : (4, 6, 3, 2), 
	'417' : (4, 6, 3, 3), 
	'418' : (4, 6, 3, 4), 
	'419' : (4, 6, 3, 5), 
	'42' : (0, 6, 6, 4), 
	'420' : (4, 6, 3, 6), 
	'421' : (4, 6, 3, 7), 
	'422' : (4, 6, 4, 6), 
	'423' : (4, 6, 5, 6), 
	'424' : (4, 6, 6, 0), 
	'425' : (4, 6, 6, 2), 
	'426' : (4, 6, 6, 3), 
	'427' : (4, 6, 6, 4), 
	'428' : (4, 6, 6, 5), 
	'429' : (4, 6, 6, 6), 
	'43' : (0, 6, 6, 5), 
	'430' : (4, 6, 6, 7), 
	'431' : (4, 6, 6, 8), 
	'432' : (4, 6, 6, 10), 
	'433' : (4, 6, 6, 11), 
	'434' : (4, 6, 7, 6), 
	'435' : (4, 6, 8, 6), 
	'436' : (4, 6, 10, 2), 
	'437' : (4, 6, 10, 3), 
	'438' : (4, 6, 10, 5), 
	'439' : (4, 6, 10, 6), 
	'44' : (0, 6, 6, 6), 
	'440' : (4, 6, 10, 10), 
	'441' : (4, 6, 11, 2), 
	'442' : (4, 6, 11, 3), 
	'443' : (4, 10, 2, 6), 
	'444' : (4, 10, 3, 2), 
	'445' : (4, 10, 3, 6), 
	'446' : (4, 10, 6, 6), 
	'447' : (4, 10, 10, 3), 
	'448' : (4, 10, 10, 6), 
	'449' : (4, 10, 10, 10), 
	'45' : (0, 6, 6, 7), 
	'450' : (4, 11, 3, 2), 
	'451' : (5, 2, 6, 2), 
	'452' : (5, 2, 6, 3), 
	'453' : (5, 2, 6, 4), 
	'454' : (5, 2, 6, 5), 
	'455' : (5, 2, 6, 6), 
	'456' : (5, 2, 6, 7), 
	'457' : (5, 3, 2, 2), 
	'458' : (5, 3, 2, 3), 
	'459' : (5, 3, 2, 6), 
	'46' : (0, 6, 6, 8), 
	'460' : (5, 3, 2, 10), 
	'461' : (5, 3, 3, 0), 
	'462' : (5, 3, 3, 2), 
	'463' : (5, 3, 3, 6), 
	'464' : (5, 3, 3, 7), 
	'465' : (5, 3, 5, 6), 
	'466' : (5, 3, 6, 0), 
	'467' : (5, 3, 6, 2), 
	'468' : (5, 3, 6, 3), 
	'469' : (5, 3, 6, 6), 
	'47' : (0, 6, 6, 10), 
	'470' : (5, 3, 6, 10), 
	'471' : (5, 6, 0, 6), 
	'472' : (5, 6, 2, 2), 
	'473' : (5, 6, 2, 3), 
	'474' : (5, 6, 2, 5), 
	'475' : (5, 6, 2, 6), 
	'476' : (5, 6, 2, 7), 
	'477' : (5, 6, 2, 10), 
	'478' : (5, 6, 3, 0), 
	'479' : (5, 6, 3, 2), 
	'48' : (0, 6, 6, 11), 
	'480' : (5, 6, 3, 3), 
	'481' : (5, 6, 3, 4), 
	'482' : (5, 6, 3, 5), 
	'483' : (5, 6, 3, 6), 
	'484' : (5, 6, 3, 7), 
	'485' : (5, 6, 3, 10), 
	'486' : (5, 6, 4, 6), 
	'487' : (5, 6, 5, 2), 
	'488' : (5, 6, 5, 3), 
	'489' : (5, 6, 5, 6), 
	'49' : (0, 6, 7, 3), 
	'490' : (5, 6, 5, 10), 
	'491' : (5, 6, 5, 11), 
	'492' : (5, 6, 6, 0), 
	'493' : (5, 6, 6, 2), 
	'494' : (5, 6, 6, 3), 
	'495' : (5, 6, 6, 4), 
	'496' : (5, 6, 6, 5), 
	'497' : (5, 6, 6, 6), 
	'498' : (5, 6, 6, 7), 
	'499' : (5, 6, 6, 8), 
	'5' : (0, 2, 6, 7), 
	'50' : (0, 6, 7, 6), 
	'500' : (5, 6, 6, 9), 
	'501' : (5, 6, 6, 10), 
	'502' : (5, 6, 6, 11), 
	'503' : (5, 6, 7, 3), 
	'504' : (5, 6, 7, 6), 
	'505' : (5, 6, 7, 10), 
	'506' : (5, 6, 8, 6), 
	'507' : (5, 6, 9, 2), 
	'508' : (5, 6, 9, 6), 
	'509' : (5, 6, 10, 0), 
	'51' : (0, 6, 8, 6), 
	'510' : (5, 6, 10, 2), 
	'511' : (5, 6, 10, 3), 
	'512' : (5, 6, 10, 5), 
	'513' : (5, 6, 10, 6), 
	'514' : (5, 6, 10, 10), 
	'515' : (5, 6, 10, 11), 
	'516' : (5, 6, 11, 0), 
	'517' : (5, 6, 11, 2), 
	'518' : (5, 6, 11, 3), 
	'519' : (5, 6, 11, 6), 
	'52' : (0, 6, 9, 2), 
	'520' : (5, 6, 11, 10), 
	'521' : (5, 6, 11, 11), 
	'522' : (5, 9, 2, 9), 
	'523' : (5, 9, 6, 2), 
	'524' : (5, 9, 6, 6), 
	'525' : (5, 9, 6, 9), 
	'526' : (5, 10, 2, 6), 
	'527' : (5, 10, 3, 2), 
	'528' : (5, 10, 3, 5), 
	'529' : (5, 10, 3, 6), 
	'53' : (0, 6, 10, 0), 
	'530' : (5, 10, 6, 2), 
	'531' : (5, 10, 6, 6), 
	'532' : (5, 10, 10, 2), 
	'533' : (5, 10, 10, 3), 
	'534' : (5, 10, 10, 6), 
	'535' : (5, 10, 10, 10), 
	'536' : (5, 11, 6, 0), 
	'537' : (5, 11, 6, 2), 
	'538' : (5, 11, 6, 3), 
	'539' : (5, 11, 6, 4), 
	'54' : (0, 6, 10, 2), 
	'540' : (5, 11, 6, 5), 
	'541' : (5, 11, 6, 6), 
	'542' : (5, 11, 6, 7), 
	'543' : (5, 11, 6, 10), 
	'544' : (6, 0, 2, 6), 
	'545' : (6, 0, 3, 0), 
	'546' : (6, 0, 3, 2), 
	'547' : (6, 0, 3, 3), 
	'548' : (6, 0, 3, 6), 
	'549' : (6, 0, 3, 7), 
	'55' : (0, 6, 10, 3), 
	'550' : (6, 0, 3, 10), 
	'551' : (6, 0, 6, 0), 
	'552' : (6, 0, 6, 2), 
	'553' : (6, 0, 6, 3), 
	'554' : (6, 0, 6, 4), 
	'555' : (6, 0, 6, 5), 
	'556' : (6, 0, 6, 6), 
	'557' : (6, 0, 6, 7), 
	'558' : (6, 0, 6, 8), 
	'559' : (6, 0, 6, 9), 
	'56' : (0, 6, 10, 6), 
	'560' : (6, 0, 6, 10), 
	'561' : (6, 0, 6, 11), 
	'562' : (6, 0, 10, 2), 
	'563' : (6, 0, 10, 3), 
	'564' : (6, 0, 10, 6), 
	'565' : (6, 0, 10, 10), 
	'566' : (6, 0, 11, 6), 
	'567' : (6, 0, 11, 11), 
	'568' : (6, 2, 2, 2), 
	'569' : (6, 2, 2, 6), 
	'57' : (0, 6, 10, 7), 
	'570' : (6, 2, 3, 0), 
	'571' : (6, 2, 3, 2), 
	'572' : (6, 2, 3, 3), 
	'573' : (6, 2, 3, 4), 
	'574' : (6, 2, 3, 6), 
	'575' : (6, 2, 3, 7), 
	'576' : (6, 2, 5, 6), 
	'577' : (6, 2, 6, 0), 
	'578' : (6, 2, 6, 2), 
	'579' : (6, 2, 6, 3), 
	'58' : (0, 6, 10, 10), 
	'580' : (6, 2, 6, 4), 
	'581' : (6, 2, 6, 5), 
	'582' : (6, 2, 6, 6), 
	'583' : (6, 2, 6, 7), 
	'584' : (6, 2, 6, 8), 
	'585' : (6, 2, 6, 9), 
	'586' : (6, 2, 6, 10), 
	'587' : (6, 2, 6, 11), 
	'588' : (6, 2, 7, 6), 
	'589' : (6, 2, 9, 2), 
	'59' : (0, 6, 11, 2), 
	'590' : (6, 2, 9, 3), 
	'591' : (6, 2, 9, 6), 
	'592' : (6, 2, 10, 2), 
	'593' : (6, 2, 10, 3), 
	'594' : (6, 2, 10, 6), 
	'595' : (6, 2, 10, 10), 
	'596' : (6, 2, 11, 2), 
	'597' : (6, 2, 11, 3), 
	'598' : (6, 2, 11, 6), 
	'599' : (6, 3, 0, 2), 
	'6' : (0, 3, 0, 6), 
	'60' : (0, 6, 11, 3), 
	'600' : (6, 3, 0, 3), 
	'601' : (6, 3, 0, 6), 
	'602' : (6, 3, 0, 10), 
	'603' : (6, 3, 2, 2), 
	'604' : (6, 3, 2, 3), 
	'605' : (6, 3, 2, 6), 
	'606' : (6, 3, 2, 10), 
	'607' : (6, 3, 2, 11), 
	'608' : (6, 3, 3, 0), 
	'609' : (6, 3, 3, 2), 
	'61' : (0, 6, 11, 5), 
	'610' : (6, 3, 3, 3), 
	'611' : (6, 3, 3, 4), 
	'612' : (6, 3, 3, 5), 
	'613' : (6, 3, 3, 6), 
	'614' : (6, 3, 3, 7), 
	'615' : (6, 3, 3, 11), 
	'616' : (6, 3, 4, 2), 
	'617' : (6, 3, 4, 3), 
	'618' : (6, 3, 4, 6), 
	'619' : (6, 3, 4, 10), 
	'62' : (0, 6, 11, 6), 
	'620' : (6, 3, 5, 2), 
	'621' : (6, 3, 5, 3), 
	'622' : (6, 3, 5, 6), 
	'623' : (6, 3, 5, 10), 
	'624' : (6, 3, 5, 11), 
	'625' : (6, 3, 6, 0), 
	'626' : (6, 3, 6, 2), 
	'627' : (6, 3, 6, 3), 
	'628' : (6, 3, 6, 4), 
	'629' : (6, 3, 6, 5), 
	'63' : (0, 6, 11, 10), 
	'630' : (6, 3, 6, 6), 
	'631' : (6, 3, 6, 7), 
	'632' : (6, 3, 6, 8), 
	'633' : (6, 3, 6, 10), 
	'634' : (6, 3, 6, 11), 
	'635' : (6, 3, 7, 2), 
	'636' : (6, 3, 7, 3), 
	'637' : (6, 3, 7, 6), 
	'638' : (6, 3, 8, 6), 
	'639' : (6, 3, 9, 2), 
	'64' : (0, 10, 2, 6), 
	'640' : (6, 3, 9, 3), 
	'641' : (6, 3, 10, 2), 
	'642' : (6, 3, 10, 3), 
	'643' : (6, 3, 10, 5), 
	'644' : (6, 3, 10, 6), 
	'645' : (6, 3, 10, 10), 
	'646' : (6, 3, 11, 2), 
	'647' : (6, 3, 11, 5), 
	'648' : (6, 3, 11, 6), 
	'649' : (6, 3, 11, 10), 
	'65' : (0, 10, 3, 2), 
	'650' : (6, 4, 2, 6), 
	'651' : (6, 4, 3, 2), 
	'652' : (6, 4, 3, 3), 
	'653' : (6, 4, 3, 6), 
	'654' : (6, 4, 6, 0), 
	'655' : (6, 4, 6, 2), 
	'656' : (6, 4, 6, 3), 
	'657' : (6, 4, 6, 4), 
	'658' : (6, 4, 6, 5), 
	'659' : (6, 4, 6, 6), 
	'66' : (0, 10, 3, 3), 
	'660' : (6, 4, 6, 7), 
	'661' : (6, 4, 6, 8), 
	'662' : (6, 4, 6, 10), 
	'663' : (6, 4, 6, 11), 
	'664' : (6, 4, 10, 2), 
	'665' : (6, 4, 10, 3), 
	'666' : (6, 4, 10, 6), 
	'667' : (6, 4, 10, 10), 
	'668' : (6, 4, 11, 3), 
	'669' : (6, 5, 2, 6), 
	'67' : (0, 10, 3, 6), 
	'670' : (6, 5, 3, 2), 
	'671' : (6, 5, 3, 3), 
	'672' : (6, 5, 3, 6), 
	'673' : (6, 5, 6, 0), 
	'674' : (6, 5, 6, 2), 
	'675' : (6, 5, 6, 3), 
	'676' : (6, 5, 6, 4), 
	'677' : (6, 5, 6, 5), 
	'678' : (6, 5, 6, 6), 
	'679' : (6, 5, 6, 7), 
	'68' : (0, 10, 6, 2), 
	'680' : (6, 5, 6, 8), 
	'681' : (6, 5, 6, 9), 
	'682' : (6, 5, 6, 10), 
	'683' : (6, 5, 6, 11), 
	'684' : (6, 5, 9, 2), 
	'685' : (6, 5, 9, 6), 
	'686' : (6, 5, 10, 2), 
	'687' : (6, 5, 10, 3), 
	'688' : (6, 5, 10, 6), 
	'689' : (6, 5, 10, 10), 
	'69' : (0, 10, 6, 3), 
	'690' : (6, 5, 11, 6), 
	'691' : (6, 6, 0, 2), 
	'692' : (6, 6, 0, 3), 
	'693' : (6, 6, 0, 6), 
	'694' : (6, 6, 0, 10), 
	'695' : (6, 6, 0, 11), 
	'696' : (6, 6, 2, 2), 
	'697' : (6, 6, 2, 3), 
	'698' : (6, 6, 2, 5), 
	'699' : (6, 6, 2, 6), 
	'7' : (0, 3, 2, 3), 
	'70' : (0, 10, 6, 6), 
	'700' : (6, 6, 2, 7), 
	'701' : (6, 6, 2, 9), 
	'702' : (6, 6, 2, 10), 
	'703' : (6, 6, 2, 11), 
	'704' : (6, 6, 3, 0), 
	'705' : (6, 6, 3, 2), 
	'706' : (6, 6, 3, 3), 
	'707' : (6, 6, 3, 4), 
	'708' : (6, 6, 3, 5), 
	'709' : (6, 6, 3, 6), 
	'71' : (0, 10, 10, 2), 
	'710' : (6, 6, 3, 7), 
	'711' : (6, 6, 3, 8), 
	'712' : (6, 6, 3, 9), 
	'713' : (6, 6, 3, 10), 
	'714' : (6, 6, 3, 11), 
	'715' : (6, 6, 4, 2), 
	'716' : (6, 6, 4, 3), 
	'717' : (6, 6, 4, 6), 
	'718' : (6, 6, 4, 10), 
	'719' : (6, 6, 5, 2), 
	'72' : (0, 10, 10, 3), 
	'720' : (6, 6, 5, 3), 
	'721' : (6, 6, 5, 6), 
	'722' : (6, 6, 5, 10), 
	'723' : (6, 6, 5, 11), 
	'724' : (6, 6, 6, 0), 
	'725' : (6, 6, 6, 2), 
	'726' : (6, 6, 6, 3), 
	'727' : (6, 6, 6, 4), 
	'728' : (6, 6, 6, 5), 
	'729' : (6, 6, 6, 6), 
	'73' : (0, 10, 10, 6), 
	'730' : (6, 6, 6, 7), 
	'731' : (6, 6, 6, 8), 
	'732' : (6, 6, 6, 9), 
	'733' : (6, 6, 6, 10), 
	'734' : (6, 6, 6, 11), 
	'735' : (6, 6, 7, 2), 
	'736' : (6, 6, 7, 3), 
	'737' : (6, 6, 7, 6), 
	'738' : (6, 6, 7, 7), 
	'739' : (6, 6, 7, 10), 
	'74' : (0, 10, 10, 10), 
	'740' : (6, 6, 7, 11), 
	'741' : (6, 6, 8, 2), 
	'742' : (6, 6, 8, 6), 
	'743' : (6, 6, 8, 10), 
	'744' : (6, 6, 9, 2), 
	'745' : (6, 6, 9, 3), 
	'746' : (6, 6, 9, 6), 
	'747' : (6, 6, 10, 2), 
	'748' : (6, 6, 10, 3), 
	'749' : (6, 6, 10, 5), 
	'75' : (0, 11, 6, 0), 
	'750' : (6, 6, 10, 6), 
	'751' : (6, 6, 10, 7), 
	'752' : (6, 6, 10, 8), 
	'753' : (6, 6, 10, 10), 
	'754' : (6, 6, 10, 11), 
	'755' : (6, 6, 11, 0), 
	'756' : (6, 6, 11, 2), 
	'757' : (6, 6, 11, 3), 
	'758' : (6, 6, 11, 6), 
	'759' : (6, 6, 11, 7), 
	'76' : (0, 11, 6, 2), 
	'760' : (6, 6, 11, 10), 
	'761' : (6, 6, 11, 11), 
	'762' : (6, 7, 2, 6), 
	'763' : (6, 7, 3, 0), 
	'764' : (6, 7, 3, 2), 
	'765' : (6, 7, 3, 3), 
	'766' : (6, 7, 3, 6), 
	'767' : (6, 7, 3, 10), 
	'768' : (6, 7, 6, 0), 
	'769' : (6, 7, 6, 2), 
	'77' : (0, 11, 6, 3), 
	'770' : (6, 7, 6, 3), 
	'771' : (6, 7, 6, 4), 
	'772' : (6, 7, 6, 5), 
	'773' : (6, 7, 6, 6), 
	'774' : (6, 7, 6, 7), 
	'775' : (6, 7, 6, 8), 
	'776' : (6, 7, 6, 9), 
	'777' : (6, 7, 6, 10), 
	'778' : (6, 7, 6, 11), 
	'779' : (6, 7, 7, 6), 
	'78' : (0, 11, 6, 6), 
	'780' : (6, 7, 9, 2), 
	'781' : (6, 7, 9, 6), 
	'782' : (6, 7, 10, 2), 
	'783' : (6, 7, 10, 3), 
	'784' : (6, 7, 10, 6), 
	'785' : (6, 7, 10, 10), 
	'786' : (6, 7, 10, 11), 
	'787' : (6, 7, 11, 3), 
	'788' : (6, 7, 11, 6), 
	'789' : (6, 7, 11, 11), 
	'79' : (0, 11, 11, 11), 
	'790' : (6, 8, 2, 6), 
	'791' : (6, 8, 3, 2), 
	'792' : (6, 8, 3, 6), 
	'793' : (6, 8, 6, 2), 
	'794' : (6, 8, 6, 3), 
	'795' : (6, 8, 6, 4), 
	'796' : (6, 8, 6, 5), 
	'797' : (6, 8, 6, 6), 
	'798' : (6, 8, 6, 7), 
	'799' : (6, 8, 6, 8), 
	'8' : (0, 3, 2, 6), 
	'80' : (2, 2, 2, 6), 
	'800' : (6, 8, 6, 10), 
	'801' : (6, 8, 6, 11), 
	'802' : (6, 8, 10, 2), 
	'803' : (6, 8, 10, 3), 
	'804' : (6, 8, 10, 6), 
	'805' : (6, 8, 10, 10), 
	'806' : (6, 8, 11, 2), 
	'807' : (6, 8, 11, 6), 
	'808' : (6, 9, 2, 6), 
	'809' : (6, 9, 2, 9), 
	'81' : (2, 2, 3, 2), 
	'810' : (6, 9, 3, 2), 
	'811' : (6, 9, 3, 6), 
	'812' : (6, 9, 3, 7), 
	'813' : (6, 9, 6, 2), 
	'814' : (6, 9, 6, 3), 
	'815' : (6, 9, 6, 6), 
	'816' : (6, 9, 6, 7), 
	'817' : (6, 9, 6, 9), 
	'818' : (6, 9, 6, 10), 
	'819' : (6, 9, 7, 6), 
	'82' : (2, 2, 3, 6), 
	'820' : (6, 9, 9, 7), 
	'821' : (6, 10, 0, 6), 
	'822' : (6, 10, 0, 10), 
	'823' : (6, 10, 2, 6), 
	'824' : (6, 10, 3, 0), 
	'825' : (6, 10, 3, 2), 
	'826' : (6, 10, 3, 3), 
	'827' : (6, 10, 3, 4), 
	'828' : (6, 10, 3, 5), 
	'829' : (6, 10, 3, 6), 
	'83' : (2, 2, 6, 0), 
	'830' : (6, 10, 3, 7), 
	'831' : (6, 10, 3, 8), 
	'832' : (6, 10, 3, 10), 
	'833' : (6, 10, 3, 11), 
	'834' : (6, 10, 5, 6), 
	'835' : (6, 10, 5, 10), 
	'836' : (6, 10, 6, 0), 
	'837' : (6, 10, 6, 2), 
	'838' : (6, 10, 6, 3), 
	'839' : (6, 10, 6, 4), 
	'84' : (2, 2, 6, 2), 
	'840' : (6, 10, 6, 5), 
	'841' : (6, 10, 6, 6), 
	'842' : (6, 10, 6, 7), 
	'843' : (6, 10, 6, 8), 
	'844' : (6, 10, 6, 9), 
	'845' : (6, 10, 6, 10), 
	'846' : (6, 10, 6, 11), 
	'847' : (6, 10, 7, 3), 
	'848' : (6, 10, 7, 6), 
	'849' : (6, 10, 7, 10), 
	'85' : (2, 2, 6, 3), 
	'850' : (6, 10, 8, 6), 
	'851' : (6, 10, 8, 10), 
	'852' : (6, 10, 10, 2), 
	'853' : (6, 10, 10, 3), 
	'854' : (6, 10, 10, 5), 
	'855' : (6, 10, 10, 6), 
	'856' : (6, 10, 10, 7), 
	'857' : (6, 10, 10, 8), 
	'858' : (6, 10, 10, 10), 
	'859' : (6, 10, 10, 11), 
	'86' : (2, 2, 6, 4), 
	'860' : (6, 10, 11, 2), 
	'861' : (6, 10, 11, 3), 
	'862' : (6, 10, 11, 6), 
	'863' : (6, 10, 11, 10), 
	'864' : (6, 10, 11, 11), 
	'865' : (6, 11, 0, 6), 
	'866' : (6, 11, 2, 3), 
	'867' : (6, 11, 2, 6), 
	'868' : (6, 11, 2, 11), 
	'869' : (6, 11, 3, 0), 
	'87' : (2, 2, 6, 5), 
	'870' : (6, 11, 3, 2), 
	'871' : (6, 11, 3, 3), 
	'872' : (6, 11, 3, 6), 
	'873' : (6, 11, 3, 7), 
	'874' : (6, 11, 3, 10), 
	'875' : (6, 11, 3, 11), 
	'876' : (6, 11, 5, 6), 
	'877' : (6, 11, 5, 11), 
	'878' : (6, 11, 6, 2), 
	'879' : (6, 11, 6, 3), 
	'88' : (2, 2, 6, 6), 
	'880' : (6, 11, 6, 5), 
	'881' : (6, 11, 6, 6), 
	'882' : (6, 11, 6, 7), 
	'883' : (6, 11, 6, 8), 
	'884' : (6, 11, 6, 10), 
	'885' : (6, 11, 6, 11), 
	'886' : (6, 11, 7, 6), 
	'887' : (6, 11, 7, 11), 
	'888' : (6, 11, 8, 6), 
	'889' : (6, 11, 10, 2), 
	'89' : (2, 2, 6, 7), 
	'890' : (6, 11, 10, 3), 
	'891' : (6, 11, 10, 6), 
	'892' : (6, 11, 10, 10), 
	'893' : (6, 11, 10, 11), 
	'894' : (6, 11, 11, 2), 
	'895' : (6, 11, 11, 3), 
	'896' : (6, 11, 11, 6), 
	'897' : (6, 11, 11, 7), 
	'898' : (6, 11, 11, 10), 
	'899' : (6, 11, 11, 11), 
	'9' : (0, 3, 3, 0), 
	'90' : (2, 2, 6, 9), 
	'900' : (7, 2, 6, 0), 
	'901' : (7, 2, 6, 2), 
	'902' : (7, 2, 6, 3), 
	'903' : (7, 2, 6, 5), 
	'904' : (7, 2, 6, 6), 
	'905' : (7, 2, 6, 7), 
	'906' : (7, 3, 0, 6), 
	'907' : (7, 3, 2, 2), 
	'908' : (7, 3, 2, 3), 
	'909' : (7, 3, 2, 6), 
	'91' : (2, 2, 7, 6), 
	'910' : (7, 3, 3, 2), 
	'911' : (7, 3, 3, 5), 
	'912' : (7, 3, 3, 6), 
	'913' : (7, 3, 3, 7), 
	'914' : (7, 3, 6, 2), 
	'915' : (7, 3, 6, 3), 
	'916' : (7, 3, 6, 6), 
	'917' : (7, 3, 6, 7), 
	'918' : (7, 3, 6, 10), 
	'919' : (7, 3, 7, 6), 
	'92' : (2, 3, 0, 6), 
	'920' : (7, 3, 10, 3), 
	'921' : (7, 6, 0, 6), 
	'922' : (7, 6, 0, 11), 
	'923' : (7, 6, 2, 2), 
	'924' : (7, 6, 2, 3), 
	'925' : (7, 6, 2, 5), 
	'926' : (7, 6, 2, 6), 
	'927' : (7, 6, 2, 10), 
	'928' : (7, 6, 3, 0), 
	'929' : (7, 6, 3, 2), 
	'93' : (2, 3, 2, 2), 
	'930' : (7, 6, 3, 3), 
	'931' : (7, 6, 3, 4), 
	'932' : (7, 6, 3, 5), 
	'933' : (7, 6, 3, 6), 
	'934' : (7, 6, 3, 7), 
	'935' : (7, 6, 3, 8), 
	'936' : (7, 6, 3, 9), 
	'937' : (7, 6, 3, 10), 
	'938' : (7, 6, 4, 2), 
	'939' : (7, 6, 4, 6), 
	'94' : (2, 3, 2, 3), 
	'940' : (7, 6, 5, 6), 
	'941' : (7, 6, 5, 10), 
	'942' : (7, 6, 5, 11), 
	'943' : (7, 6, 6, 0), 
	'944' : (7, 6, 6, 2), 
	'945' : (7, 6, 6, 3), 
	'946' : (7, 6, 6, 4), 
	'947' : (7, 6, 6, 5), 
	'948' : (7, 6, 6, 6), 
	'949' : (7, 6, 6, 7), 
	'95' : (2, 3, 2, 6), 
	'950' : (7, 6, 6, 8), 
	'951' : (7, 6, 6, 9), 
	'952' : (7, 6, 6, 10), 
	'953' : (7, 6, 6, 11), 
	'954' : (7, 6, 7, 2), 
	'955' : (7, 6, 7, 3), 
	'956' : (7, 6, 7, 6), 
	'957' : (7, 6, 7, 7), 
	'958' : (7, 6, 7, 9), 
	'959' : (7, 6, 7, 10), 
	'96' : (2, 3, 2, 10), 
	'960' : (7, 6, 7, 11), 
	'961' : (7, 6, 8, 6), 
	'962' : (7, 6, 8, 11), 
	'963' : (7, 6, 9, 2), 
	'964' : (7, 6, 9, 3), 
	'965' : (7, 6, 9, 6), 
	'966' : (7, 6, 10, 2), 
	'967' : (7, 6, 10, 3), 
	'968' : (7, 6, 10, 5), 
	'969' : (7, 6, 10, 6), 
	'97' : (2, 3, 3, 0), 
	'970' : (7, 6, 10, 7), 
	'971' : (7, 6, 10, 10), 
	'972' : (7, 6, 10, 11), 
	'973' : (7, 6, 11, 2), 
	'974' : (7, 6, 11, 3), 
	'975' : (7, 6, 11, 6), 
	'976' : (7, 6, 11, 7), 
	'977' : (7, 6, 11, 10), 
	'978' : (7, 6, 11, 11), 
	'979' : (7, 7, 6, 3), 
	'98' : (2, 3, 3, 2), 
	'980' : (7, 9, 2, 6), 
	'981' : (7, 9, 2, 9), 
	'982' : (7, 9, 6, 3), 
	'983' : (7, 9, 6, 6), 
	'984' : (7, 9, 6, 7), 
	'985' : (7, 10, 2, 6), 
	'986' : (7, 10, 3, 2), 
	'987' : (7, 10, 3, 6), 
	'988' : (7, 10, 6, 2), 
	'989' : (7, 10, 6, 3), 
	'99' : (2, 3, 3, 3), 
	'990' : (7, 10, 6, 6), 
	'991' : (7, 10, 6, 7), 
	'992' : (7, 10, 10, 2), 
	'993' : (7, 10, 10, 3), 
	'994' : (7, 10, 10, 6), 
	'995' : (7, 10, 10, 10), 
	'996' : (7, 10, 11, 3), 
	'997' : (7, 11, 2, 6), 
	'998' : (7, 11, 3, 2), 
	'999' : (7, 11, 6, 2), 
}