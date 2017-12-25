# -*- coding: utf-8 -*-

# Scrapy settings for articalScrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os
BOT_NAME = 'articalScrapy'

SPIDER_MODULES = ['articalScrapy.spiders']
NEWSPIDER_MODULE = 'articalScrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'articalScrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'articalScrapy.middlewares.ArticalscrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'articalScrapy.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {     #此处代码本来就用，只需要解除注释
   # 'articalScrapy.pipelines.JsonExporterPipeline': 2,
   # 'articalScrapy.pipelines.ArticleImagePipeline': 1,
   # 'articalScrapy.pipelines.MysqlPipeline': 1,
   'articalScrapy.pipelines.MysqlTwistedPipeline': 1,
   # 'scrapy.pipelines.images.ImagesPipeline': 1,   # 设置image的pipeline,数字越小优先级越高
}
IMAGES_URLS_FIELD = "front_img_url"   #设置图片的参数
project_dir=os.path.abspath(os.path.dirname(__file__))   #获取父路径
IMAGES_STORE = os.path.join(project_dir,"imgs")   #设置最终的图片存储路径

IMAGE_MIN_WIDTH= 100
IMAGE_MIN_HEIGHT= 100 #设置图片尺寸最小为100*100

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# MYSQL_HOST = "192.168.0.114"
# MYSQL_DBNAME = "articlespider"
# MYSQL_USER = "root"
# MYSQL_PASSWORD = "xjl1994920"
# MYSQL_PORT = 3336

# MYSQL_HOST = "121.196.194.14"
# MYSQL_DBNAME = "articlespider"
# MYSQL_USER = "root"
# MYSQL_PASSWORD = "lytech"
# MYSQL_PORT = 3336

# vultr
MYSQL_HOST = "172.17.0.4"
MYSQL_DBNAME = "jobbole"
MYSQL_USER = "root"
MYSQL_PASSWORD = "123456789"
MYSQL_PORT = 3306