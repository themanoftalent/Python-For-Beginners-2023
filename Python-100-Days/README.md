## Python-100 days from novice to master

> Author: Luo Hao
>
> Recently, many friends who want to learn Python have joined our communication group one after another. At present, our communication group has more than 10,000 people. Our goal is to create a high-quality Python communication community. On the one hand, it clears the obstacles in the process of getting started for beginners who want to learn Python; on the other hand, it provides a way for new developers to ask questions and help them quickly grow into excellent ones. Professionals; In addition, experienced developers can use this platform to share or provide their work experience for free, so that everyone can get a comprehensive promotion of professional skills and comprehensive quality. The previous public classes and offline technical exchange activities have been abandoned for some time because of work. However, the small partners are still active in the communication group and support us as always, thank you here. Recently, the content of the first 15 days and the last 10 days has been continuously updated. The first 15 days are written for beginners. I hope that the difficulty of getting started will be further reduced, and the example program will be simpler and clearer. The last 10 days are related to the actual combat of Python projects and interviews. I hope that the content is more detailed and complete, especially the interview question on the 100th day. It ’s not easy to create. Thank you for your support. The money will not be used to buy coffee but will be donated to the people in need through the Tencent public welfare platform. ([Click] (./ update log.md) for donations).

! [] (./ res / python-qq-group.png)

### Analysis of Python application areas and employment situation

Simply put, Python is an "elegant", "clear", and "simple" programming language.

 -Low learning curve for non-professionals
 -Open source system with strong ecosystem
 -Interpreted language, perfect platform portability
 -Supports object-oriented and functional programming
 -Ability to extend functions by calling C / C ++ code
 -High degree of code specification and readability

Python is currently in use in several popular areas.

 -Cloud Infrastructure-Python / Java / Go
 -DevOps-Python / Shell / Ruby / Go
 -Web crawler-Python / PHP / C ++
 -Data Analysis Mining-Python / R / Scala / Matlab
 -Machine Learning-Python / R / Java / Lisp

As a Python developer, the main employment areas include:

-Python server background development / game server development / data interface development engineer
-Python Automation Operation and Maintenance Engineer
-Python data analysis / data visualization / big data engineer
-Python Crawler Engineer
-Python chat robot development / image recognition and vision algorithms / deep learning engineers

The chart below shows the Python recruitment demand and salary rankings of major cities (as of May 2018).

! [Python Recruitment Demand and Salary Top 10] (./ res / python-top-10.png)

! [] (./ res / python-bj-salary.png)

! [] (./ res / python-salary-chengdu.png)

A few suggestions for beginners:

-Make English as your working language.
-Practice makes perfect.
-All experience comes from mistakes.
-Don't be one of the leeches.
-Either stand out or kicked out.

### Day01 ~ 15-[Python Language Basics] (./ Day01-15)

#### Day01-[Meeting Python] (Day01-15 / 01.Python.md)

-Introduction to Python-History of Python / Advantages and disadvantages of Python / Application areas of Python
-Build programming environment-Windows environment / Linux environment / MacOS environment
-Run Python program from terminal-Hello, world / print function / Run program
-Using IDLE-Interactive environment (REPL) / Writing multiple lines of code / Running a program / Exiting IDLE
-Comments-The role of comments / single-line comments / multi-line comments

#### Day02-[Language Elements] (Day01-15 / 02.LanguageElements.md)

-Programs and bases-Instructions and programs / Von Neumann machines / Binary and decimal / Octal and hexadecimal
-Variables and types-Variable naming / Use of variables / Input functions / Checking variable types / Type conversion
-Numbers and strings-Integers / Floating point numbers / Complex numbers / Strings / String basic operations / Character encoding
-Operators-Mathematical operators / Assignment operators / Comparison operators / Logical operators / Identity operators / Operator precedence
-Application Case-Convert Fahrenheit to Celsius / Enter the radius of a circle to calculate the perimeter and area / Enter the year

#### Day03-[Branch Structure] (./ Day01-15 / 03.Branch Structure.md)

-Application scenarios of branch structure-Conditions / Indentation / Code block / Flow chart
-if statement-simple if / if-else structure / if-elif-else structure / nested if
-Application examples-User authentication / Swap the imperial unit and the metric unit / Roll the dice to decide what to do / Percentage to grade system / Segmentation function evaluation / Enter the length of the three sides to calculate the circumference and area

#### Day04-[Loop Structure] (./ Day01-15 / 04.Loop Structure.md)

-Application scenarios for loop structures-Conditions / indentation / code blocks / flow diagrams
-while loop-basic structure / break statement / continue statement
-for loop-basic structure / range type / branch structure in loop / nested loop / end program early
-Application Cases-1 ~ 100 Summation / Judging Prime Numbers / Guessing Numbers Game / Printing Nine or Nine Tables / Printing Triangle Patterns / Monkey Eating Peach / Money and Money

#### Day05-[Constructor Logic] (./ Day01-15 / 05.Constructor Logic.md)

-Classic case: Number of daffodils / 100 bucks / 100 chickens / Craps gambling game
-Exercise: Fibonacci sequence / perfect number / prime number

#### Day06-[Use of functions and modules] (./ Day01-15 / 06. Use of functions and modules.md)

-The role of functions-Bad smell of code / Encapsulation of functional modules with functions
-Define function-def statement / function name / parameter list / return statement / call custom function
-Call functions-Python built-in functions / import modules and functions
-Function parameters-default parameters / variable parameters / keyword parameters / named keyword parameters
-The return value of the function-no return value / single value returned / multiple values ​​returned
-Scope issues-local scope / nested scope / global scope / built-in scope / scope related keywords
-Manage functions with modules-Module concepts / Manage functions with custom modules / What happens when naming conflicts (same module and different modules)

#### Day07-[Strings and common data structures] (./ Day01-15 / 07.Strings and common data structures.md)

-Use of strings-Calculate length / subscript operation / slicing / common methods
-Basic usage of lists-Definition of lists / Accessing elements with the table below / Subscripts crossing boundaries / Adding elements / Deleting elements / Modifying elements / Slicing / Looping
-List common operations-Join / Copy (copy elements and copy arrays) / length / sort / reverse / find
-Generate list-Create number list using range / Generate expression / Generator
-Use of tuples-Define tuples / Use values ​​in tuples / Modify tuple variables / Tuple and list conversion
-Basic collection usage-Difference between collection and list / Create collection / Add element / Remove element / Empty
-Set common operations-Intersection / Union / Difference / Symmetric Difference / Subset / Superset
-Basic usage of dictionary-Features of dictionary / Create dictionary / Add element / Delete element / Value / Clear
-Common dictionary operations-keys () method / values ​​() method / items () method / setdefault () method
-Basic exercises-Marquee effect / Find the biggest element in the list / Statistics average score of the test score / Fibonacci sequence / Yang Hui triangle
-Comprehensive case-Two-color ball selection / Tic-tac-toe

#### Day08-[Object-oriented programming basics] (./ Day01-15 / 08. Object-oriented programming basics.md)

-Classes and objects-What is a class / What is an object / Other object-oriented concepts
-Defining classes-Basic structure / Properties and methods / Constructors / Destructors / \ _ \ _ str \ _ \ _ methods
-Working with objects-Creating objects / Sending messages to objects
-Four pillars of object-oriented-abstraction / encapsulation / inheritance / polymorphism
-Basic Exercises-Define Student Class / Define Clock Class / Define Graphics Class / Define Automotive Class

#### Day09-[Advanced Object Orientation] (./ Day01-15 / 09. Advanced Object Orientation.md)

-Attributes-Class Attributes / Instance Attributes / Attribute Accessors / Attribute Modifiers / Attribute Deleters / Use \ _ \ _ slots \ _ \ _
-Methods in the class-Instance methods / Class methods / Static methods
-Operator overloading-\ _ \ _ add \ _ \ _ / \ _ \ _ sub \ _ \ _ / \ _ \ _ or \ _ \ _ / \ _ \ _ getitem \ _ \ _ / \ _ \ _ setitem \ _ \ _ / \ _ \ _ len \ _ \ _ / \ _ \ _ repr \ _ \ _ / \ _ \ _ gt \ _ \ _ / \ _ \ _ lt \ _ \ _ / \ _ \ _ le \ _ \ _ / \ _ \ _ ge \ _ \ _ / \ _ \ _ eq \ _ \ _ / \ _ \ _ ne \ _ \ _ / \ _ \ _ contains \ _ \ _
-Relationship between classes (objects)-Association / Inheritance / Dependency
-Inheritance and polymorphism-What is inheritance / Inheritance syntax / Calling parent method / Method rewriting / Type determination / Multiple inheritance / Diamond inheritance (diamond inheritance) and C3 algorithm
-Comprehensive case-Payroll settlement system / automatic book discount system / custom scores

#### Day10-[Graphical User Interface and Game Development] (./ Day01-15 / 10. Graphic User Interface and Game Development.md)

-Use tkinter to develop GUI programs
-Use pygame library to develop game applications
-"Big Ball Eat Small Ball" game

#### Day11-[Files and Exceptions] (./ Day01-15 / 11.Files and Exceptions.md)

-Read file-Read entire file / Read line by line / File path
-Write file-Overwrite / Append / Text file / Binary file
-Exception Handling-Importance of exception mechanism / try-except code block / else code block / finally code block / built-in exception type / exception stack / raise statement
-Data Persistence-CSV file overview / application of csv module / JSON data format / application of json module

#### Day12-[Strings and regular expressions] (./Day01-15/12. Strings and regular expressions. Md)

-Advanced string operations-Escape characters / raw strings / multi-line strings / in and not in operators / methods beginning with is / join and split methods / strip related methods / pyperclip module / immutable strings and mutable String / StringIO usage
-Getting started with regular expressions-What regular expressions do / metacharacters / escapes / quantifiers / groupings / zero-width assertions / greedy matching and lazy matching laziness / regular expression operations (match, search, replace, capture) using the re module
-Use regular expressions-re modules / compile functions / group and groups methods / match methods / search methods / findall and finder methods / sub and subn methods / split methods
-Application case-Validate input string using regular expression

#### Day13-[Processes and Threads] (./ Day01-15 / 1

-The concept of processes and threads-What is a process / What is a thread / Multi-threaded application scenario
-Use process-fork function / multiprocessing module / process pool / inter-process communication
-Using threads-thread module / threading module / Thread class / Lock class / Condition class / Thread pool

#### Day14-[Introduction to Network Programming and Network Application Development] (./ Day01-15 / 14. Introduction to Network Programming and Network Application Development.md)

-Computer Network Basics-History of Computer Network Development / "TCP-IP" Model / IP Address / Port / Protocol / Other Related Concepts
-Network Application Mode-"Client-Server" Mode / "Browser-Server" Mode
-Access network resources based on HTTP protocol-Overview of network API / Access URL / requests module / Parse JSON format data
-Python Network Programming-Socket Concept / Socket Module / Socket Function / Create TCP Server / Create TCP Client / Create UDP Server / Create UDP Client / SocketServer Module
-Email-SMTP protocol / POP3 protocol / IMAP protocol / smtplib module / poplib module / imaplib module
-SMS Service-Call SMS Service Gateway

#### Day15-[Image and Document Processing] (./ Day01-15 / 15. Image and Office Document Processing.md)

-Process pictures with Pillow-Picture reading and writing / picture composition / geometric transformation / color transformation / filter effect
-Read and write Word documents-Handle text content / Paragraphs / Headers and footers / Styles
-Read and write Excel files-xlrd module / xlwt module
-Generate PDF file-pypdf2 module / reportlab module

### Day16 ~ Day20-[Advanced Python Language] (./ Day16-20 / 16-20.Advanced Python Language.md)

-Common data structures
-Advanced usage of functions-"First-class citizens" / Higher-order functions / Lambda functions / Scopes and closures / Decorators
-Advanced Object-Oriented Knowledge-"Three Pillars" / The Relationship Between Classes / Garbage Collection / Magic Properties and Methods / Hybrids / Metaclasses / Object-Oriented Design Principles / GoF Design Patterns
-Iterators and generators-Related magic methods / Two ways to create generators /
-Concurrent and asynchronous programming-multi-threaded / multi-process / asynchronous IO / async and await

### Day21 ~ 30-[Getting Started with Web Front End] (./ Day21-30 / 21-30.Web Front End Overview.md)

-Host page content with HTML tags
-Render pages with CSS
-Handle interactive behavior with JavaScript
-jQuery entry and improvement
-Getting started with Vue.js
-Use of Element
-Use of Bootstrap

### Day31 ~ 35-[Fun Linux Operating System] (./ Day31-35 / 31-35.Fun Linux Operating System.md)

-Operating system history and Linux overview
-Linux basic commands
-Utilities in Linux
-Linux file system
-Application of Vim editor
-Environment variables and shell programming
-Software installation and service configuration
-Network access and management
-Other related content

### Day36 ~ 40-[Database Basics and Advanced] (./ Day36-40)

-[Relational Database MySQL] (./ Day36-40 / 36-38.Relational Database MySQL.md)
  -Overview of relational databases
  -MySQL installation and use
  -Use of SQL
    -DDL-Data Definition Language-create / drop / alter
    -DML-Data Manipulation Language-insert / delete / update / select
    -DCL-Data Control Language-grant / revoke
  - related information
    -Paradigm Theory-Guidelines for Designing Two-Dimensional Tables
    -Data integrity
    -Data consistency
  -Operate MySQL in Python
-[Getting Started with NoSQL] (./ Day36-40 / 39-40.NoSQL Getting Started.md)
  -NoSQL Overview
  -Redis overview
  -Mongo overview

### Day41 ~ 55-[Combat Django] (./ Day41-55)

#### Day41-[Quick Start] (./Day41-55/41. Quick Start.md)

-Web application working principle and HTTP protocol
-Overview of the Django framework
-Get started in 5 minutes
-Use view templates

#### Day42-[Deep Model] (./ Day41-55 / 42.Deep Model.md)

-Relational database configuration
-Manage background usage
-Use ORM to complete CRUD operations on the model
-Django model best practices
-Model definition reference

#### Day43-[static resources and Ajax requests] (./ Day41-55 / 43.static resources and Ajax requests.md)

-Load static resources
-Get data with Ajax request

#### Day44-[Application of form] (./ Day41-55 / 44. Application of form.md)

-Forms and form controls
-Cross-site request forgery and CSRF token
-Form and ModelForm
- form validation

#### Day45-[Cookie and Session] (./ Day41-55 / 45.Cookie and Session.md)

-Implement user tracking
-The relationship between cookies and sessions
-Django framework support for sessions
-Read and write cookies in view functions

#### Day46-[Reports and Logs] (./ Day41-55 / 46.Reports and Logs.md)

-Modify response header via HttpResponse
-Use StreamingHttpResponse for large files
-Generate Excel report using xlwt
-Generate PDF reports using reportlab
-Generate front-end charts with ECharts
-Configure logs and Django-Debug-Toolbar

#### Day47-[Application of Middleware] (./ Day41-55 / 47. Application of Middleware.md)

-What is middleware
-Middleware built into the Django framework
-Custom middleware and its application scenarios

#### Day48-[Getting Started With Front-End Separation Development] (./Day41-55/48. Getting Started With Front-End Separation Development.md)

-Returns data in JSON format
-Render pages with Vue.js

#### Day49-[Getting Started with RESTful Architecture and DRF] (./ Day41-55 / 49.Getting Started with RESTful Architecture and DRF.md)

#### Day50-[RESTful architecture and advanced DRF] (./ Day41-55 / 50.RESTful architecture and advanced DRF.md)

#### Day51-[use cache] (./ Day41-55 / 51.use cache.md)

-First Law of Website Optimization

-Use Redis to provide caching services in Django projects
-Read and write cache in view functions
-Implement page caching using decorators
-Provide cache service for data interface

#### Day52-[File upload and rich text editing] (./ Day41-55 / 52.File upload and rich text editor.md)

-File upload form control and picture file preview
-How the server handles uploaded files
-Rich text editor overview
-Use of wangEditor

#### Day53-[SMS & Email] (./ Day41-55 / 53.SMS & Email.md)

-Introduction of Common SMS Gateway Platforms
-Send SMS using screw cap
-Django framework support for mail services

#### Day54-[Asynchronous and Timed Tasks] (./ Day41-55 / 54.Asynchronous and Timed Tasks.md)

-Website Optimization Second Law
-Configure the message queue service
-Use celery to make tasks asynchronous in projects
-Use celery to implement timed tasks in projects

#### Day55-[Unit testing and project launch] (./Day41-55/55. Unit testing and project launch.md)

-Unit tests in Python
-Django framework support for unit testing
-Use a version control system
-Configure and use uWSGI
-Dynamic and static separation and Nginx configuration
-Configure HTTPS


### Day56 ~ 60-[Actual Flask] (./ Day56-65)

#### Day56-[Flask Getting Started] (./ Day56-60 / 56.Flask Getting Started.md)

#### Day57-[Use of template] (./ Day56-60 / 57. Use of template.md)

#### Day58-[Form Processing] (./Day56-60/58. Form Processing.md)

#### Day59-[Database Operations] (./ Day56-60 / 59.Database Operations.md)

#### Day60-[Project Combat] (./ Day56-60 / 60. Project Combat.md)

### Day61 ~ 65-[Actual Tornado] (./ Day61-65)

#### Day61-[Preliminary Knowledge] (./ Day61-65 / 61.Preliminary Knowledge.md)

-Concurrent programming
-I / O mode and event driven

#### Day62-[Getting Started With Tornado] (./ Day61-65 / 62.Getting Started With Tornado.md)

-Tornado overview
-5 minutes to get started with Tornado
-Route resolution
-Request handler

#### Day63-[Asynchronous] (./ Day61-65 / 63.Asynchronous.md)

-Use of aiomysql and aioredis

#### Day64-[Application of WebSocket] (./ Day61-65 / 64.Application of WebSocket.md)

-Introduction to WebSocket
-WebSocket server programming
-WebSocket Client Programming
-Project: Web chat room

#### Day65-[Project combat] (./ Day61-65 / 65.Project combat.md)

-Separate front-end and back-end development
-Front-end rendering with Vue.js
-Use ECharts for reporting
-Push service using WebSocket

### Day66 ~ 75-[Reptile Development] (./ Day66-75)

#### Day66-[Crawlers and related tools] (./ Day66-75 / 66.Crawlers and related tools.md)

-The concept of web crawler and its application field
-Discussion on the legitimacy of web crawlers
-Develop related tools for web crawlers
-The composition of a crawler program

#### Day67-[Data Collection and Analysis] (./ Day66-75 / 67.Data Collection and Analysis.md)

-Standard and tripartite libraries for data collection
-Three ways of page parsing: regular expression parsing / XPath parsing / CSS selector parsing

#### Day68-[Storage Data] (./ Day66-75 / 68. Storage Data.md)

-How to store massive data
-Implement data caching

#### Day69-[Concurrent download] (./ Day66-75 / 69.Concurrent download.md)

-Multi-threaded and multi-process
-Asynchronous I / O and coroutines
-Use of async and await keywords
-Application of three party library aiohttp

#### Day70-[parse dynamic content] (./ Day66-75 / 70.parse dynamic content.md)

-JavaScript reverse engineering
-Get dynamic content with Selenium

#### Day71-[Form interaction and verification code processing] (./ Day66-75 / 71. Form interaction and verification code processing.md)

-Auto submit form
-Cookie Pool Application
-Verification code processing

#### Day72-[Getting started with Scrapy] (./ Day66-75 / 72.Getting started with Scrapy.md)

-Overview of Scrapy crawler framework
-Install and use Scrapy

#### Day73-[Scrapy Advanced Application] (./ Day66-75 / 73.Scrapy Advanced Application.md)

-Spider usage
-Application of middleware: download middleware

#### Day74-[Scrapy distributed implementation] (./ Day66-75 / 74.Scrapy distributed implementation.md)

-Principles of distributed crawlers
-Scrapy distributed implementation
-Distributed deployment with Scrapyd

#### Day75-[Crawler Project Combat] (./ Day66-75 / 75.Crawler Project Combat.md)

-Crawling recruitment site data
-Crawl real estate industry data
-Crawling used car trading platform data

### Day76 ~ 90-[Data Processing and Machine Learning] (./ Day76-90)

#### Day76-[Machine Learning Basics] (./ Day76-90 / 76.Machine Learning Basics.md)

#### Day77-[Application of Pandas] (./ Day76-90 / 77.Application of Pandas.md)

#### Day78-[Application of NumPy and SciPy] (./Day76-90/78. Application of NumPy and SciPy)

#### Day79-[Matplotlib and data visualization] (./Day76-90/79.Matplotlib and data visualization)

#### Day80-[k nearest neighbor (KNN) classification] (./ Day76-90 / 80.k nearest neighbor classification.md)

#### Day81-[Decision Tree] (./ Day76-90 / 81. Decision Tree.md)

#### Day82-[Bayesian Classification] (./ Day76-90 / 82.Bayesian Classification.md)

#### Day83-[Support Vector Machine (SVM)] (./ Day76-90 / 83. Support Vector Machine.md)

#### Day84-[K-means clustering] (./ Day76-90 / 84.K-means clustering.md)

#### Day85-[Regression Analysis] (./ Day76-90 / 85.Regression Analysis.md)

#### Day86-[Introduction to Big Data Analysis] (./ Day76-90 / 86.Introduction to Big Data Analysis.md)

#### Day87-[Advanced Big Data Analysis] (./ Day76-90 / 87.Advanced Big Data Analysis.md)

#### Day88-[Getting Started With Tensorflow] (./ Day76-90 / 88.Getting Started With Tensorflow.md)

#### Day89-[Tensorflow combat] (./Day76-90/89.Tensorflow combat.md)

#### Day90-[Recommendation System] (./ Day76-90 / 90.Recommendation System.md)

### Day91 ~ 100-[Team Project Development] (./ Day91-100)

#### Day 91: [Questions and solutions for team project development] (./ Day91-100 / 91. Problems and solutions for team project development.md)

Software process model
   -Classic process model (waterfall model)
     -Feasibility analysis (do or don't do research), output "feasibility analysis report".
     -Requirements analysis (study what to do), output "Requirement Specification" and product interface prototype diagram.
     -Outline design and detailed design, output conceptual model diagram (ER diagram), physical model diagram, class diagram, timing diagram, etc.
     -Coding / testing.
     -Go live / maintain.

     The biggest shortcoming of the waterfall model is that it cannot embrace changes in demand. The product can only be seen after the entire process is completed, and the morale of the team is low.
   -Scrum-Product Owner, Scrum Master, R & D Staff-Sprint
     -Product Backlog (user story, product prototype).
     -Planning meetings (evaluation and budget).
     -Daily development (stand-up meetings, tomato work, pair programming, test-first, code refactoring ...).
     -Fix bugs (problem descriptions, steps to reproduce, testers, assignees).
     - release version.
     -Review meeting (Showcase, users need to participate).
     -Retrospective (to summarize the current iteration cycle).

     > Added: Manifesto for Agile Software Development
     >
     >-** Individual and interactive ** above processes and tools
     >-** Working Software ** Above detailed documentation
     >-** Customer cooperation ** higher than contract negotiation
     >-** response to change ** higher than follow plan

     ! [] (./ res / agile-scrum-sprint-cycle.png)

     > Role: Product owner (who decides what to do and who can make a decision), team leader (solve various issues, focus on how to work better, shield the external influence on the development team), development team (project executive) , Specifically developers and testers).

     > Preparations: business case and funding, contract, vision, initial product requirements, initial release plan, shareholding, team formation.

     > Agile teams usually have 8-10 people.

     > Estimation of workload: Quantify development tasks, including prototypes, logo design, UI design, front-end development, etc., and try to break down each task to the minimum task amount. The minimum task amount standard is that the working time cannot exceed two days, and then estimate the overall project. time. Stick each task on the Kanban board, which is divided into three parts: to do (to be completed), in progress (done) and done (completed).

2. Project team formation

   -Team composition and roles

     > Explanation: Thank you, Ms. Fu Xiangying for drawing this beautiful organization chart.

     ! [company_architecture] (./ res / company_architecture.png)

   -Programming specifications and code review (flake8, pylint)

     ! [] (./ res / pylint.png)

   -Some "conventions" in Python (please refer to ["Python Conventions-How to Write Pythonic Code"] (Python Conventions.md)

   -Reasons affecting code readability:

     -Too few or no comments
     -Code breaks language best practices
     -Anti-pattern programming (spaghetti code, copy-paste programming, conceit programming, ...)

3. Team Development Tools
   -Version control: Git, Mercury
   -Defect management: [Gitlab] (https://about.gitlab.com/), [Redmine] (http://www.redmine.org.cn/)
   -Agile closed-loop tools: [Zhendao] (https://www.zentao.net/), [JIRA] (https://www.atlassian.com/software/jira/features)
   -Continuous integration: [Jenkins] (https://jenkins.io/), [Travis-CI] (https://travis-ci.org/)

   Please refer to ["Problems and Solutions for Team Project Development"] (Day91-100 / 91. Problems and Solutions for Team Project Development. Md).

##### Project selection and understanding of business

Setting of choice

   -CMS (user terminal): news aggregation site, Q & A / share community, film review / book review site, etc.
   -MIS (user side + management side): KMS, KPI assessment system, HRS, CRM system, supply chain system, warehouse management system, etc.

   -App background (management terminal + data interface): second-hand transactions, newspapers and magazines, niche e-commerce, news and information, travel, social, reading, etc.
   -Other types: own industry background and work experience, business is easy to understand and control.

2. Requirements understanding, module division and task allocation

   -Demand understanding: brainstorming and competitive product analysis.
   -Module division: draw a mind map (XMind), each module is a branch node, and each specific function is a leaf node (expressed with a verb). You need to ensure that each leaf node cannot reproduce new nodes, and determine The importance, priority, and workload of leaf nodes.
   -Task assignment: The project leader assigns tasks to each team member based on the above indicators.

   ! [] (./ res / requirements_by_xmind.png)

3. Develop project schedule (updated daily)

   Module | Function | Personnel | Status | Completed | Work Hours | Planned Start | Actual Started |
   | ---- | -------- | ------ | -------- | ---- | ---- | -------- | -------- | -------- | -------- | ---------------- |
   | Comments | Add Comments | King Sledgehammer | In Progress | 50% | 4 | 8/7/2018 |
   | Remove Comment | King Sledgehammer | Waiting | 0% | 2 | 8/7/2018 | | 8/7/2018 |
   | View comments | Bai Yuanfang | Ongoing | 20% | 4 | 8/7/2018 | | 8/7/2018 |
   | Poll | Bai Yuanfang | Waiting | 0% | 4 | 8/8/2018 | | 8/8/2018 |

4. OOAD and database design

  -Class diagram of UML (Unified Modeling Language)

    ! [uml] (./ res / uml-class-diagram.png)

  -Creating tables from models (forward engineering)

    `` `Shell
    python manage.py makemigrations app
    python manage.py migrate
    `` `

  -Use PowerDesigner to draw physical model diagrams.

    ! [] (./ res / power-designer-pdm.png)

  -Creating models from data tables (reverse engineering)

    `` `Shell
    python manage.py inspectdb> app / models.py
    `` `

#### Day 92: [Detailed explanation of Docker container] (./ Day91-100 / 92.Detailed explanation of Docker container.md)

1. Introduction to Docker
2. Install Docker
3. Create containers using Docker (Nginx, MySQL, Redis, Gitlab, Jenkins)
4. Build a Docker image (writing of Dockerfile and related instructions)
5. Container Orchestration (Docker-compose)
6. Cluster management

#### Day 93: [MySQL Performance Optimization] (./ Day91-100 / 93.MySQL Performance Optimization.md)

#### Day 94: [Network API Interface Design] (./ Day91-100 / 94.Network API Interface Design.md)

#### Day 95: [Develop commercial projects with Django] (./ Day91-100 / 95. Developing commercial projects with Django.md)

##### Public issues in project development

1. Database configuration (multi-database, master-slave replication, database routing)
2. Cache configuration (partition cache, key settings, timeout settings, master-slave replication, failure recovery (sentinel))
3. Log configuration
4. Analysis and debugging (Django-Debug-ToolBar)
5. Easy-to-use Python modules (date calculation, image processing, data encryption, tripartite API)

##### REST API Design

RESTful architecture
   -[Understanding RESTful Architecture] (http://www.ruanyifeng.com/blog/2011/09/restful.html)
   -[RESTful API Design Guide] (http://www.ruanyifeng.com/blog/2014/05/restful_api.html)
   -[RESTful API Best Practices] (http://www.ruanyifeng.com/blog/2018/10/restful-api