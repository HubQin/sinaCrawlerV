CREATE TABLE if not exists `wb_mzm_post` (
`id` bigint(16) unsigned NOT NULL auto_increment COMMENT '木子美微博',
`post_id` bigint(16) unsigned NOT NULL,
`content` text NOT NULL,
`add_time` int(10),
`attitudes_count` int(10),
`comments_count` int(10),
`retweet_content` text NULL,
PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;

CREATE TABLE if not exists `wb_mzm_comment` (
`id` bigint(16) unsigned NOT NULL auto_increment COMMENT '木子美微博评论',
`post_id` bigint(16) unsigned NOT NULL,
`comment_id` bigint(16) unsigned NOT NULL,
`comment_user_id` bigint(16) unsigned NOT NULL,
`comment_user_name` varchar(50),
`text` text,
`reply_text` text,
`user_photo` text,
`user_profile` text,
`add_time` int(10),
`like_count` int(10),
PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;

CREATE TABLE if not exists `wb_mzm_article` (
`id` bigint(16) unsigned NOT NULL auto_increment COMMENT '木子美文章',
`article_id` bigint(16) unsigned NOT NULL,
`text` text,
`add_time` int(10),
PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;