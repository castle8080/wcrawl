
## Features

* Core Storage
    * Queue Publish & Subscribe
        * Basic Use [done]
        * Handle de-dup [in progress]
        * Check RabbitMQ best practices such as utilize shared connections. [todo]
        * Deal with long queue - lazy queues and durability [todo]
        * idea: randomize task execution across domains to lower load on a single site? (means an ordered queue isn't quite right)
    * Blob Store
        * Basic FileSystem [done]
        * Add auto compression [todo]
        * Add directory partitioning [todo]
* Download URL
    * Basic download and storage [done]
    * check robots.txt [todo]
    * add rate limiter

* Content Processing
    * Link Extraction [in progress]
        * parse html for links [in progress] (need to process base tag still)
    * Link download queue [depends on queue deduping]

* Startup
    * startup script [todo]
    * logging-setup [todo]

## Current Priority Task

Basic download is working with ability to extract links. Before automatically starting to crawl, need dedupping of the queue and checking robots.txt. 
