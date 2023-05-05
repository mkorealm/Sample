-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Май 05 2023 г., 06:22
-- Версия сервера: 8.0.19
-- Версия PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `sample`
--

DELIMITER $$
--
-- Процедуры
--
CREATE DEFINER=`mkorealm`@`localhost` PROCEDURE `get_user` ()  NO SQL
SELECT * FROM user$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Структура таблицы `counter`
--

CREATE TABLE `counter` (
  `count` mediumint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `counter`
--

INSERT INTO `counter` (`count`) VALUES
(0);

-- --------------------------------------------------------

--
-- Дублирующая структура для представления `get_user`
-- (См. Ниже фактическое представление)
--
CREATE TABLE `get_user` (
`id_user` smallint unsigned
,`name` varchar(45)
,`surname` varchar(45)
,`email` varchar(50)
,`phone` varchar(13)
,`passport` varchar(10)
,`login` varchar(16)
,`password` varchar(16)
,`create_date` datetime
,`last_update` timestamp
);

-- --------------------------------------------------------

--
-- Структура таблицы `user`
--

CREATE TABLE `user` (
  `id_user` smallint UNSIGNED NOT NULL,
  `name` varchar(45) NOT NULL,
  `surname` varchar(45) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(13) NOT NULL,
  `passport` varchar(10) NOT NULL,
  `login` varchar(16) NOT NULL,
  `password` varchar(16) NOT NULL,
  `create_date` datetime NOT NULL,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `user`
--

INSERT INTO `user` (`id_user`, `name`, `surname`, `email`, `phone`, `passport`, `login`, `password`, `create_date`, `last_update`) VALUES
(1, 'Максим', 'Королев', 'mkorealm@gmail.com', '90118178782', '1023021221', 'mkorealm', 'mk!!2011', '2023-05-05 06:08:39', '2023-05-05 03:08:39');

--
-- Триггеры `user`
--
DELIMITER $$
CREATE TRIGGER `counter` AFTER INSERT ON `user` FOR EACH ROW UPDATE counter SET count=(count+1)
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `counter2` AFTER DELETE ON `user` FOR EACH ROW UPDATE counter SET count=(count-1)
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Структура для представления `get_user`
--
DROP TABLE IF EXISTS `get_user`;

CREATE ALGORITHM=UNDEFINED DEFINER=`mkorealm`@`localhost` SQL SECURITY DEFINER VIEW `get_user`  AS SELECT `user`.`id_user` AS `id_user`, `user`.`name` AS `name`, `user`.`surname` AS `surname`, `user`.`email` AS `email`, `user`.`phone` AS `phone`, `user`.`passport` AS `passport`, `user`.`login` AS `login`, `user`.`password` AS `password`, `user`.`create_date` AS `create_date`, `user`.`last_update` AS `last_update` FROM `user` ;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `user`
--
ALTER TABLE `user`
  MODIFY `id_user` smallint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
