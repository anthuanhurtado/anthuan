-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-03-2017 a las 20:17:03
-- Versión del servidor: 10.1.16-MariaDB
-- Versión de PHP: 5.6.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `productos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productoss`
--

CREATE TABLE `productoss` (
  `id_producto` int(2) NOT NULL,
  `productos` varchar(20) NOT NULL,
  `descripcion` varchar(20) NOT NULL,
  `existencias` float NOT NULL,
  `precio_compra` float NOT NULL,
  `precio_venta` float NOT NULL,
  `imagen_producto` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `productoss`
--

INSERT INTO `productoss` (`id_producto`, `productos`, `descripcion`, `existencias`, `precio_compra`, `precio_venta`, `imagen_producto`) VALUES
(1, 'xbox', 'One', 10, 750, 1000, 'xboxone.png'),
(2, 'audifonos', 'chicharo', 20, 350, 500, 'audifonos.png'),
(3, 'Balon', 'Nike', 5, 180, 250, 'balon.png'),
(4, 'Lentes', 'Gota', 15, 65, 100, 'lente.png');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `productoss`
--
ALTER TABLE `productoss`
  ADD PRIMARY KEY (`id_producto`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `productoss`
--
ALTER TABLE `productoss`
  MODIFY `id_producto` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
