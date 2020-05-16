/*
Navicat MySQL Data Transfer

Source Server         : git
Source Server Version : 50727
Source Host           : localhost:3306
Source Database       : bim_db

Target Server Type    : MYSQL
Target Server Version : 50727
File Encoding         : 65001

Date: 2020-05-16 20:45:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for image_path
-- ----------------------------
DROP TABLE IF EXISTS `image_path`;
CREATE TABLE `image_path` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `belong` varchar(255) DEFAULT NULL,
  `pid` int(11) DEFAULT '0',
  `belong_id` int(11) DEFAULT '0',
  `image_name` varchar(255) DEFAULT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `vedio_up_url` varchar(255) DEFAULT NULL,
  `vedio_left_url` varchar(255) DEFAULT NULL,
  `vedio_right_url` varchar(255) DEFAULT NULL,
  `vedio_bottom_url` varchar(255) DEFAULT NULL,
  `abstract` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of image_path
-- ----------------------------
INSERT INTO `image_path` VALUES ('9', '通航孔桥钢梁附属设施', '0', null, '阻尼安装示意图', '', null, null, null, null, null);
INSERT INTO `image_path` VALUES ('10', '通航孔桥钢梁附属设施', '9', null, '3-3断面', '3-3断面.jpg', '', '', '', '', null);
INSERT INTO `image_path` VALUES ('11', '通航孔桥钢梁附属设施', '9', null, '2-2断面', '2-2断面.jpg', '', '', '', '', null);
INSERT INTO `image_path` VALUES ('12', '通航孔桥钢梁附属设施', '0', null, '挡砟墙', null, null, null, null, null, null);
INSERT INTO `image_path` VALUES ('13', '通航孔桥钢梁附属设施', '12', null, '挡砟墙横截面', '挡砟墙横截面.jpg', '', '', '', '', null);
INSERT INTO `image_path` VALUES ('15', '健康监测系统预留件', '0', null, '鼓屿门水道桥道砟预埋镀锌钢管布置图', '/健康监测系统预留件/JPZ8XOdFIEQpu9w0tDLRz3KH.png', '/健康监测系统预留件/jw3EDSQ4VmBoO8HiAR5FWayY.mp4', '/健康监测系统预留件/CQ5x3zAEtiueHOJj0XfvUakY.mp4', null, '/健康监测系统预留件/PunrXBfqWSLEZx9Rhl58dzbt.mp4', '1');
INSERT INTO `image_path` VALUES ('16', '健康监测系统预留件', '0', null, '鼓屿门水道桥预留件M1', '/健康监测系统预留件/u8eMYiL0Fyt7maTz1Qdx2JGZ.png', null, null, null, null, '测试');
INSERT INTO `image_path` VALUES ('17', '健康监测系统预留件', '0', null, '鼓屿门水道桥预留件M2M6', '/健康监测系统预留件/knpiF3j40YoeufHxaDgvZwAL.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('18', '健康监测系统预留件', '0', null, '鼓屿门水道桥预留件M3M6', '/健康监测系统预留件/izrDToNWmQ0JudVYaXOgjCKf.png', null, null, null, null, '11');
INSERT INTO `image_path` VALUES ('19', '健康监测系统预留件', '0', null, '鼓屿门水道桥预留件M4M5M6', '/健康监测系统预留件/DIn4aHkUSdqhCuf0Yc3sLirJ.png', null, null, null, null, '测试');
INSERT INTO `image_path` VALUES ('20', '健康监测系统预留件', '0', null, '鼓屿门水道桥预留件M6M7', '/健康监测系统预留件/TYuzbiwW3tf7SQoJmcEjICP0.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('21', '健康监测系统预留件', '0', null, '鼓屿门水道桥预留桥架', '/健康监测系统预留件/Pqi5Ev6ob9U7mMDcIyF0SXwY.png', null, null, null, null, '2');
INSERT INTO `image_path` VALUES ('22', '健康监测系统预留件', '0', null, '元洪航道桥槽式桥梁', '/健康监测系统预留件/rSsnFXOuhbDgMfpjcH4JwQy1.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('23', '健康监测系统预留件', '0', null, '元洪航道桥道碴槽预埋钢管布置图', '/健康监测系统预留件/icOE5bVJMCowPx9Iqj4HaNtn.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('24', '健康监测系统预留件', '0', null, '元洪航道桥预留件M1布置图', '/健康监测系统预留件/QOPTn9U7k1xgYKWIqBsy8Npl.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('25', '健康监测系统预留件', '0', null, '元洪航道桥预留件M2布置图', '/健康监测系统预留件/LNxFwfZh7Uv1IPRa5AdprV2j.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('26', '健康监测系统预留件', '0', null, '元洪航道桥预留件M5布置图', '/健康监测系统预留件/7Bt51MHLjDsfKFbuCG3Rqxzr.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('27', '健康监测系统预留件', '0', null, '元洪航道桥预留件M6布置图', '/健康监测系统预留件/Y1Nmga9IvC5PFf8zVlEjJwXO.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('28', '健康监测系统预留件', '0', null, '元洪航道桥预留件M7布置图', '/健康监测系统预留件/OwdqMTreo4ak3ZPyD9BY8pXG.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('29', '桥梁综合接地', '0', null, 'N03号墩基础接地图', '/桥梁综合接地/qpeXR7Ouv4cZJoATVCfjBs28.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('30', '桥梁综合接地', '0', null, 'N04号墩基础接地图', '/桥梁综合接地/H8cWoNrXbmnGUdyzf7l2wKqO.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('31', '桥梁综合接地', '0', null, 'S03号墩基础接地图', '/桥梁综合接地/A7lM64i8bQWujqNkGRfhwJmV.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('32', '桥梁综合接地', '0', null, 'S04号墩基础接地图', '/桥梁综合接地/yAZWejPxqpwktsiIrzGf4uo3.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('33', '健康监测系统预留件', '0', null, '元洪航道桥预留件M8布置图', '/健康监测系统预留件/f7x9h4qPdSewGFUKtTQXmNI1.png', null, null, null, null, '1');
