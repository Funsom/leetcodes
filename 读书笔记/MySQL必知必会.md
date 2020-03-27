# MySQL必知必会 读书笔记
## 第一章 了解数据库
+ 数据库 保存有组织的数据的容器，通常是一个文件或一组文件
+ 表 某种特定类型数据的结构化清单
+ 模式（schema）关于数据库和表的布局及特性的信息
+ 列 （column）表中的一个字段。所有表都是由一个或多个列组成的 可以理解为字段？
+ 数据类型 所容许的数据的类型。每个表列都有相应的数据类型，它限制该列中存储的数据
+ 行 表中的一个记录
+ 主键（primary key） 一列或一组列，其值能够唯一区分表中的每个行
  + 应该总是定义主键 虽然并不是总都需要主键
  + 表中的任意列都可以作为主键，只要任意两行都不相等，每行都不为NULL
  + 多列作为主键时，其组合保持唯一且不为NULL
+ 主键的最好习惯：
  + 不更新主键列中的值
  + 不重用主键列中的值
  + 不在主键列中使用可能会更改的值
+ SQL Structured Query Language 结构化查询语言
## 第二章 MySQL简介
+ MySQL选项和参数 mysql -u ben -p -h myserver -P 8080;
## 第三章 使用MySQL
+ 选择数据库 USE databaseName 必须先使用USE打开数据库，才能读取其中的数据
+ 显示可选数据库： SHOW DATABASES;
+ 显示可选表： SHOW TABLES;返回当前选择的数据库内可用的表的列表
+ 显示表列（表头，字段）： SHOW COLUMNS FROM tableName; show columns要求给出一个表名，它对每个字段返回一行，行中包含字段名，数据类型，是否允许NULL、键信息、默认值以及其他信息 DESCRIBE 是SHOW COLUMNS FROM 的一种快捷方式
+ SHOW STATUS，用于显示广泛的服务器状态信息；
+ SHOW CREATE DATABASE和 SHOW CREATE TABLE，分别用来显示创建特定数据库或表的MySQL语句
+ SHOW GRANTS，用来显示授予用户（所有用户或特定用户）的安全权限
+ SHOW REEORS和SHOW WARRNINGS, 用来显示服务器错误或警告信息。
+ 进一步了解SHOW ： HELP SHOW
## 第四章 检索数据
+ 检索单个列： SELECT name FROM table;
+ 检索多个列：SELECT name,others FROM table;
+ 检索所有列：SELECT * FROM table;
+ 检索值唯一的行 ：SELECT distinct vend_id FROM products;
+ 限制返回结果条目： SELECT name FROM products limit 5;
+ 得到5-10条数据：SELECT name FROM products limit 5,5; 返回从行5开始的5行，第一个数为开始的位置，第二个数为要检索的行数。下标从0开始，行数不够时，有多少返回多少
+ 等价表达：limit 5,5 == limit 5 offset 5
+ 使用完全限定的表名：同时使用表名和列字 SELECT products.name FROM database.products;
## 第五章 排序检索数据
+ 子句（clause）SQL语句由子句构成，有些子句是必需的，而有些是可选的。一个子句通常由一个关键字和所提供的数据组成。
+ ORDER BY子句 进行排序 SELECT name FROM database ORDER BY name;
+ 还可以通过非选择列进行排序
+ 按多个列排序 SELECT id,name price FROM database ORDER BY name,price;前一个列相同，则比较后一列，不同则只比较前一列
+ 指定排序方向 SELECT id FROM db ORDER BY name DESC; 以name降序排列，DESC仅直接作用于其前面的列名，多个列排序时，当第一列相同时，第二列要按降序排列还要用desc 。ascending 升序 descending 降序
+ 使用order by 与 limit 可以找出最值
## 第六章 过滤数据
+ 在SELECT语句中，数据根据where子句中指定的搜索条件进行过滤。where子句在表名之后给出。SELECT name FROM db WHERE name == 'tom'; 
+ ORDER BY 要在 WHERE 之后
+ ***MySQL查询语句各关键字的执行顺序***
  + 书写顺序
    + SELECT -> FROM -> WHERE -> group by -> having -> ORDER BY
    + FROM -> WHERE -> group by -> having -> SELECT -> ORDER BY
+ WHERE子句操作符 BETWEEN a AND b 在指定的两个值之间
+ SELECT price FROM produces WHERE price between 5 and 10;
+ 空值查询： select name from product where id is null;
## 第七章 数据过滤
+ AND 操作符：用于where子句中的关键字，用来指示检索满足所有给定条件的行<br>select id,name,price from products where id = 10 and price <= 10;
+ OR 操作符：用于where子句中的关键字，用来指示检索匹配任一给定条件的行<br> select id,name,price from products where id = 10 or price <= 10; 
+ 计算次序： 优先计算AND 可以使用圆括号明确地分组<br> select name,price from products where (id=1002 or id=1003) AND price >= 10;
+ 在where子句中使用圆括号，任何时候使用具有and和or操作符的where子句，都应该使用圆括号明确地分组操作符，不要过分依赖默认计算次序，即使他确实是你想要的也是如此，使用圆括号没有什么坏处，它能消除歧义。
+ IN 操作符： 用来指定条件范围，范围中的每个条件都可以进行匹配。IN取合法值的由逗号分隔的清单，全部都在圆括号中。<br> select name,price from products where id in (1002,1003) order by name; 
+ IN操作符的优点：
  + 使用长的合法选项清单时，IN操作符的语法更加清楚且直观
  + 在使用IN时，计算的次序更容易管理
  + IN操作符一般比OR操作符清单执行的更快
  + IN的最大优点是可以包括其他select语句，使得能够更动态地建立where子句
+ NOT 操作符：功能只有一个，就是否定它之后所有的任何条件<br>select name,price from products where id not in (1002,1003) order by name;
## 第八章 用通配符进行过滤
### LIKE 操作符
+ 通配符（wildcard） 用来匹配值的一部分的特殊字符
+ 搜索模式 由字面值、通配符或者两者的组合构成的搜索条件
+ 通配符本身实际上是where子句中有特殊含义的字符SQL支持如下通配符
+ 百分号通配符（%） 在搜索串中，%代表任何字符出现任意次，例如为了找出所有以jet开头的产品，可以使用一下select语句<br> select id,name from products where name like 'jet%'; 通配符可以在任意位置使用。'%anvil%' 表示匹配任何位置包含文本anvil的值 % 通配符不会匹配NULL
+ 下划线通配符（_）下划线通配符只匹配一个任意字符而不是多个字符
+ 通配符的使用是有代价的，将通配符的匹配位置放在开头是最慢的
## 第九章 用正则表达式进行搜索
+ REGEXP  
  + 进行OR匹配 
  + select name from products where name regexp '1000|2000' order by name;
  + 匹配几个字符之一
  + [123] == 1|2|3
  + 匹配范围
  + [0-9][a-z][A-Z]
  + 匹配特殊字符
  + '\\\\.'双斜杠转义 \\\\\\ 反斜杠 \\\\f 换页 \\\\n 换行 \\\\r 回车 \\\\t 制表 \\\\v 纵向制表
  + 匹配字符类
  + [:alnum:] 任意字母与数字
  + 匹配多个实例
  + \* 0到多 \+ 1到多 ? 0到1 {n} 指定数目 {n,}不少于n次 {n,m} 在范围内
  + 定位符
  + ^ 开头 $ 结尾 [[:<:]] 词的开头 [[:>:]] 词的结尾
  + LIKE与REGEXP的区别 ： LIKE匹配整个串 REGEXP匹配子串
## 第十章 创建计算字段
+ 字段(field) 基本上与column的意思相同，不过数据库列一般称为列，而术语字段通常用于在计算字段的连接上。
+ 拼接字段 concatenate Concat() select Concat(name,'(',country,')') from vendors order by name; Concat() 拼接串，即把多个串连接起来形成一个较长的串
+ RTrim(...) 去掉值右边的所有空格
+ 使用别名 AS select Concat(name,'(',country,')') as title from vendors order by name;
+ 执行算术计算 select id,quantity, price, quantity*price as expanded_price from orderitems where order_num = 20005;
## 第十一章 使用数据处理函数
+ 文本处理函数
  + Upper(...) 将文本转换成大写 
  + Left() 返回串左边的字符
  + Length() 返回串的长度
  + Locate() 找出串的一个子串
  + Lower() 将串转换为小写
  + LTrim() 去掉串左边的空格
  + Right() 返回串右边的字符
  + RTrim() 去掉串右边的空格
  + Soundex() 返回串的SOUNDEX值 SOUNDEX是一个将任何文本串转换为描述其语音表示的字母数字模式的算法
  + SubString() 返回子串的字符
+ 日期和时间处理函数
  + AddDate() AddTime() CurDate() 当前日期 CurTime() 当前时间 Date() 日期
  + DateDiff() Year() Now()
  + select id,name from orders where Date(order_date) = '2005-09-01';
  + 检索2005年9月的数据
    + select id,name from orders where Date(order_date) between '2005-09-01' and '2005-09-30';
    + select id,name from orders where Year(order_date) = 2005 and Month(order_date) = 9;
  + 数值处理函数
    + Abs() Cos() Exp() 指数值 Mod() Pi() Rand() 随机数 Sin() Sqrt() Tan()
## 第十二章 汇总数据
+ 聚合函数 aggregate function
  + AVG() COUNT() MAX() MIN() SUM() 
  + select AVG(price) AS avg_price from products where id = 1003;
  + AVG() 只能用来确定特定数值列的平均值，而且列名必须作为函数参数给出，为获得多个列的平均值必须使用多个AVG()函数 忽略NULL
  + COUNT() COUNT(*)对表中的行进行计数，COUNT(column)对指定列中具有值的行进行计数，忽略NULL select COUNT(email) as num_cust from customers;
  + MAX() 返回指定列中的最大值 select MAX(price) AS max_price from products;
+ 聚合不同值
  + select AVG(distinct price) AS avg_price from products where id = 1003;
+ 组合聚合函数
  + select COUNT(*) AS num_items,MIN(prod_price) AS price_min, MAX(prod_price) AS price_max, AVG(prod_price) AS price_avg from products;
## 第十三章 分组数据