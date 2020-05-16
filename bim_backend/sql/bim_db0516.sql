/*
Navicat MySQL Data Transfer

Source Server         : remote
Source Server Version : 50536
Source Host           : 210.34.58.5:3306
Source Database       : bim_db

Target Server Type    : MYSQL
Target Server Version : 50536
File Encoding         : 65001

Date: 2020-05-16 07:55:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admins
-- ----------------------------
DROP TABLE IF EXISTS `admins`;
CREATE TABLE `admins` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `detail` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of admins
-- ----------------------------
INSERT INTO `admins` VALUES ('3', '4344324', '$6$rounds=656000$VcaDX7pvyAiixQw1$./ENdBLR7mbj33fAp0X30aV8laZSFfPTpsFQEQgmozGJlUdEmPPlOG4.Erd4ROvU4Xf9JmWQkeYmaXR76rnnZ.', '2432443');

-- ----------------------------
-- Table structure for employee
-- ----------------------------
DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `employee_name` varchar(255) NOT NULL COMMENT '员工姓名',
  `employee_number` varchar(255) NOT NULL COMMENT '员工工号',
  `employee_tel` varchar(255) DEFAULT NULL COMMENT '员工电话',
  `employee_id_number` varchar(255) DEFAULT NULL COMMENT '岗位证号',
  `employee_dept` varchar(255) DEFAULT NULL COMMENT '部门',
  `employee_job` varchar(255) DEFAULT NULL COMMENT '负责内容',
  `employee_project` varchar(255) DEFAULT NULL COMMENT '所属施工专项',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of employee
-- ----------------------------
INSERT INTO `employee` VALUES ('1', '刘志', '000001', '15398763311', '4100002400021', '工程部', '总负责人', 'D1100-63V型塔式起重机拆卸专项');
INSERT INTO `employee` VALUES ('2', '孙光', '000002', '15398763312', '4100002400022', '工程部', '技术总负责', 'D1100-64V型塔式起重机拆卸专项');
INSERT INTO `employee` VALUES ('3', '张兴', '000003', '15398763313', '4100002400023', '工程部', '安全质量负责', 'D1100-65V型塔式起重机拆卸专项');
INSERT INTO `employee` VALUES ('4', '吴东', '000004', '15398763314', '4100002400024', '工程部', '现场负责人', 'D1100-66V型塔式起重机拆卸专项');
INSERT INTO `employee` VALUES ('5', '李飞', '000005', '15398763315', '4100002400025', '工程部', '质量管理', 'D1100-67V型塔式起重机拆卸专项');
INSERT INTO `employee` VALUES ('6', '张峰', '000006', '15398763316', '4100002400026', '工程部', '物资管理', 'D1100-68V型塔式起重机拆卸专项');
INSERT INTO `employee` VALUES ('7', '朱强\r\n', '000007', '15398763317', '4100002400027', '工程部', '设备管理', 'D1100-69V型塔式起重机拆卸专项');
INSERT INTO `employee` VALUES ('8', '叶龙\r\n', '000008', '15398763318', '4100002400028', '工程部', '设备管理', 'D1100-69V型塔式起重机拆卸专项');
INSERT INTO `employee` VALUES ('9', '\r\n张三', '000009', '15398763319', '4100002400029', '工程部', '设备管理', 'D1100-69V型塔式起重机拆卸专项');
INSERT INTO `employee` VALUES ('10', '李四', '000010', '15398763320', '4100002400030', '工程部', '设备管理', 'D1100-69V型塔式起重机拆卸专项');
INSERT INTO `employee` VALUES ('11', '王五', '000011', '15398763321', '4100002400031', '工程部', '设备管理', 'D1100-69V型塔式起重机拆卸专项');

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
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of image_path
-- ----------------------------
INSERT INTO `image_path` VALUES ('9', '通航孔桥钢梁附属设施', '0', null, '阻尼安装示意图', '', null, null, null, null, null);
INSERT INTO `image_path` VALUES ('10', '通航孔桥钢梁附属设施', '9', null, '3-3断面', '3-3断面.jpg', '', '', '', '', null);
INSERT INTO `image_path` VALUES ('11', '通航孔桥钢梁附属设施', '9', null, '2-2断面', '2-2断面.jpg', '', '', '', '', null);
INSERT INTO `image_path` VALUES ('12', '通航孔桥钢梁附属设施', '0', null, '挡砟墙', null, null, null, null, null, null);
INSERT INTO `image_path` VALUES ('13', '通航孔桥钢梁附属设施', '12', null, '挡砟墙横截面', '挡砟墙横截面.jpg', '', '', '', '', null);
INSERT INTO `image_path` VALUES ('15', '健康监测系统预留件', '0', null, '鼓屿门水道桥道砟预埋镀锌钢管布置图', '/健康监测系统预留件/JPZ8XOdFIEQpu9w0tDLRz3KH.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('16', '健康监测系统预留件', '0', null, '鼓屿门水道桥预留件M1', '/健康监测系统预留件/u8eMYiL0Fyt7maTz1Qdx2JGZ.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('17', '健康监测系统预留件', '0', null, '鼓屿门水道桥预留件M2M6', '/健康监测系统预留件/Ht1fTmZULbBh932sjMg4w0NE.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('18', '健康监测系统预留件', '0', null, '鼓屿门水道桥预留件M3M6', '/健康监测系统预留件/izrDToNWmQ0JudVYaXOgjCKf.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('19', '健康监测系统预留件', '0', null, '鼓屿门水道桥预留件M4M5M6', '/健康监测系统预留件/DIn4aHkUSdqhCuf0Yc3sLirJ.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('20', '健康监测系统预留件', '0', null, '鼓屿门水道桥预留件M6M7', '/健康监测系统预留件/TYuzbiwW3tf7SQoJmcEjICP0.png', null, null, null, null, '');
INSERT INTO `image_path` VALUES ('21', '健康监测系统预留件', '0', null, '鼓屿门水道桥预留桥架', '/健康监测系统预留件/Pqi5Ev6ob9U7mMDcIyF0SXwY.png', null, null, null, null, '');
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

-- ----------------------------
-- Table structure for participants_information
-- ----------------------------
DROP TABLE IF EXISTS `participants_information`;
CREATE TABLE `participants_information` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `participants_name` varchar(255) NOT NULL,
  `participants_sex` int(1) NOT NULL,
  `participants_tel` varchar(255) DEFAULT NULL,
  `participants_work_status` int(1) NOT NULL,
  `participants_qualification` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of participants_information
-- ----------------------------
INSERT INTO `participants_information` VALUES ('2', '2', '孙光', '0', '15398763312', '1', '教授');
INSERT INTO `participants_information` VALUES ('3', '3', '张兴', '1', '15398763313', '0', '教授');
INSERT INTO `participants_information` VALUES ('4', '3', '吴东', '0', '15398763314', '0', '副教授');
INSERT INTO `participants_information` VALUES ('5', '5', '李飞', '0', '15398763315', '0', '副教授');
INSERT INTO `participants_information` VALUES ('7', '5', '朱强\r\n', '1', '15398763317', '0', '高级工程师');
INSERT INTO `participants_information` VALUES ('8', '1', '叶龙\r\n', '1', '15398763318', '1', '初级工程师');
INSERT INTO `participants_information` VALUES ('9', '2', '张三', '1', '13075817175', '1', '教授');

-- ----------------------------
-- Table structure for project
-- ----------------------------
DROP TABLE IF EXISTS `project`;
CREATE TABLE `project` (
  `id` int(11) NOT NULL,
  `item_name` varchar(255) NOT NULL,
  `item_img_href` varchar(255) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of project
-- ----------------------------
INSERT INTO `project` VALUES ('0', '墩旁托架拆除施工', '1.jpg');
INSERT INTO `project` VALUES ('1', '移动模架（转场）拆除施工', '2.jpg');
INSERT INTO `project` VALUES ('2', '钻孔平台及栈桥拆除施工', '3.jpg');
INSERT INTO `project` VALUES ('3', 'D1100-63V型塔式起重机拆卸专项', '4.jpg');
INSERT INTO `project` VALUES ('4', '钢梁电力通道及附属结构安装专项', '5.jpg');
INSERT INTO `project` VALUES ('5', '鼓屿门水道桥公路箱梁支架法现浇专项施工', '6.jpg');

-- ----------------------------
-- Table structure for secmanager
-- ----------------------------
DROP TABLE IF EXISTS `secmanager`;
CREATE TABLE `secmanager` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `device_name` varchar(20) DEFAULT NULL,
  `specification` varchar(20) DEFAULT NULL,
  `number` int(20) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `sec_project` (`project_id`) USING BTREE,
  CONSTRAINT `sec_project` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Records of secmanager
-- ----------------------------
INSERT INTO `secmanager` VALUES ('5', '1', '苏启欣荣11（锚艇）', '20t', '3');
INSERT INTO `secmanager` VALUES ('7', '2', '中南878（锚艇）', null, '1');

-- ----------------------------
-- Table structure for sections
-- ----------------------------
DROP TABLE IF EXISTS `sections`;
CREATE TABLE `sections` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sectionsname` varchar(255) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of sections
-- ----------------------------
INSERT INTO `sections` VALUES ('1', '一区段');
INSERT INTO `sections` VALUES ('2', '二区段');
INSERT INTO `sections` VALUES ('3', '三区段');
INSERT INTO `sections` VALUES ('4', '四区段');
INSERT INTO `sections` VALUES ('5', '元洪航道段');
INSERT INTO `sections` VALUES ('6', '六区段');
INSERT INTO `sections` VALUES ('7', '鼓屿门水道段');
INSERT INTO `sections` VALUES ('8', '八区段');
INSERT INTO `sections` VALUES ('9', '九区段');
INSERT INTO `sections` VALUES ('10', '十区段');
INSERT INTO `sections` VALUES ('11', '11-14区段');
INSERT INTO `sections` VALUES ('12', '十五区段');
INSERT INTO `sections` VALUES ('13', '大小练岛水道段');
INSERT INTO `sections` VALUES ('14', '十七区段\r\n');
INSERT INTO `sections` VALUES ('15', '十八区段');

-- ----------------------------
-- Table structure for struct_info
-- ----------------------------
DROP TABLE IF EXISTS `struct_info`;
CREATE TABLE `struct_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `struct_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of struct_info
-- ----------------------------
INSERT INTO `struct_info` VALUES ('1', '分区段整体模型');
INSERT INTO `struct_info` VALUES ('2', '通航孔桥钢梁附属设施');
INSERT INTO `struct_info` VALUES ('3', '通航孔桥主塔及下部结构附属设施');
INSERT INTO `struct_info` VALUES ('4', '非通航孔桥上部结构附属设施');
INSERT INTO `struct_info` VALUES ('5', '非通航孔桥下部结构附属设施');
INSERT INTO `struct_info` VALUES ('6', '全桥风屏障及声屏障结构');
INSERT INTO `struct_info` VALUES ('7', '桥梁综合接地');
INSERT INTO `struct_info` VALUES ('8', '桥梁供电、照明');
INSERT INTO `struct_info` VALUES ('9', '健康监测系统预留件');

-- ----------------------------
-- Table structure for sub_project
-- ----------------------------
DROP TABLE IF EXISTS `sub_project`;
CREATE TABLE `sub_project` (
  `id` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `sub_project_name` varchar(255) NOT NULL,
  `sub_project_status` varchar(255) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of sub_project
-- ----------------------------
INSERT INTO `sub_project` VALUES ('0', '3', '2019-03-14 20:16:29', '2019-03-25 20:19:11', '拆除准备工作', '已完成');
INSERT INTO `sub_project` VALUES ('1', '3', '2019-03-25 20:19:11', '2019-04-22 20:19:48', '降节', '已完成');
INSERT INTO `sub_project` VALUES ('2', '3', '2019-03-28 20:20:52', '2019-04-15 20:22:25', '拆除附墙拉杆', '已完成');
INSERT INTO `sub_project` VALUES ('3', '3', '2019-04-01 20:21:09', '2019-04-18 20:22:32', '拆除附着装置', '已完成');
INSERT INTO `sub_project` VALUES ('4', '3', '2019-04-01 20:21:09', '2019-04-29 20:21:58', '拆除部件装车退场', '已完成');
INSERT INTO `sub_project` VALUES ('5', '3', '2019-04-22 20:21:39', '2019-04-28 20:22:07', '降节到最后解体', '已完成');
INSERT INTO `sub_project` VALUES ('6', '5', '2019-03-03 20:24:58', '2019-08-19 20:25:33', '左幅公路现浇施工', '已完成');
INSERT INTO `sub_project` VALUES ('7', '5', '2019-03-03 20:24:58', '2019-09-29 20:25:40', '右幅公路现浇施工', '已完成');
INSERT INTO `sub_project` VALUES ('8', '5', '2019-04-08 20:25:17', '2019-09-02 21:34:12', 'CX18~CX19支架搭设', '已完成');

-- ----------------------------
-- Table structure for sysmonitor
-- ----------------------------
DROP TABLE IF EXISTS `sysmonitor`;
CREATE TABLE `sysmonitor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sections_id` int(11) NOT NULL,
  `stresses` varchar(255) DEFAULT NULL,
  `shape` varchar(255) DEFAULT NULL,
  `temperature` varchar(255) DEFAULT NULL,
  `humidity` varchar(255) DEFAULT NULL,
  `windpower` varchar(255) DEFAULT NULL,
  `day` datetime NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of sysmonitor
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL COMMENT '用户真实姓名',
  `loginname` varchar(255) NOT NULL COMMENT '登录账号',
  `password` varchar(255) NOT NULL COMMENT '密码',
  `telphone` varchar(255) DEFAULT NULL,
  `userdetail` varchar(255) DEFAULT NULL,
  `lastlogin` datetime DEFAULT NULL,
  `company` varchar(255) DEFAULT NULL COMMENT '工作单位',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('2', null, 'sujinhe', '$6$rounds=656000$8fk70A4oo/I5Neki$iBQ6TpUKza9tjUERqWVBBuBPyP9iCjpL0NUmo3pIRdkASMu/ceFXKuhXzK1Ojs5EWgW92HfyNW0xv46xrR42f/', null, '123456', '2020-03-07 22:23:04', null);
INSERT INTO `user` VALUES ('3', null, 'gong', '$6$rounds=656000$xRN2eTaiiZUjUZMv$nI7AeTM0NEVebmSyyNa7G8rdGEA6gukmGVn2ZcIpwlqb6Cqx7L3/OAFyiwcIrF9qxuY2wgN9lEuEe3IzxS0yt.', null, '123456', '2020-03-07 22:23:59', null);
INSERT INTO `user` VALUES ('4', '苏锦河', 'admin', '$6$rounds=656000$FztYPhI8M6EDylWi$s8v8ofgwAv62TDoUBv4YBnp8yY867j3MX2Lb0XyxcjkKx65pFQPz3z/UBpWDj3Xs2cc7hHVtyBhzjxAk02SFn1', '13075717175', '超级管理员', '2020-03-08 17:39:31', '福州大学');

-- ----------------------------
-- Table structure for user_login_info
-- ----------------------------
DROP TABLE IF EXISTS `user_login_info`;
CREATE TABLE `user_login_info` (
  `id` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `logintime` datetime NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ROW_FORMAT=FIXED;

-- ----------------------------
-- Records of user_login_info
-- ----------------------------
