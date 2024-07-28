INSERT INTO products(Id,Name,Price,Count)
VALUES
(1787075,'porzkir','850000',0),
(13358923,'bigoodi','35000',4),
(2365593,'halghe taxeini','37500',2),
(5989735,'dastband','18780',300),
(8828209,'shane mo zanane','189000',3),
(8111438,'service ghazakhori','790000',100),
(1787072,'tarazoo digital','399000',0);

SELECT  * from products
where count>0;


INSERT INTO Customers(Id,Name,city,Country)
VALUES
(1,'faeze','mashhad','Iran'),
(2,'nafise','tehran','Iran'),
(3,'fateme','quchan','Iran'),
(4,'hoda','bojnord','Iran'),
(1010,'ana','torento','canada');


DELETE FROM Customers 
WHERE not Country='Iran';

UPDATE products
SET Price =Price*0.8;
