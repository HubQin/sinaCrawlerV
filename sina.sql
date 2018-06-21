CREATE DATABASE IF NOT EXISTS `weibo`;
USE `weibo`;

CREATE TABLE IF NOT EXISTS `wb_mzm_article` (
  `id` bigint(16) unsigned NOT NULL AUTO_INCREMENT,
  `article_id` varchar(30) NOT NULL,
  `title` varchar(150) CHARACTER SET utf8 NOT NULL,
  `content` text CHARACTER SET utf8 NOT NULL,
  `add_time` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `wb_mzm_comment` (
  `id` bigint(16) unsigned NOT NULL AUTO_INCREMENT,
  `post_id` bigint(16) unsigned NOT NULL,
  `comment_id` bigint(16) unsigned NOT NULL,
  `comment_user_id` bigint(16) unsigned NOT NULL,
  `comment_user_name` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `text` text,
  `reply_text` text,
  `user_photo` text CHARACTER SET utf8,
  `user_profile` text CHARACTER SET utf8,
  `add_time` int(10) DEFAULT NULL,
  `like_count` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `wb_mzm_post` (
  `id` bigint(16) unsigned NOT NULL AUTO_INCREMENT,
  `post_id` bigint(16) unsigned NOT NULL,
  `content` mediumtext NOT NULL,
  `add_time` int(10) DEFAULT NULL,
  `attitudes_count` int(10) DEFAULT NULL,
  `comments_count` int(10) DEFAULT NULL,
  `retweet_content` mediumtext,
  `retweet_id` bigint(16) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
