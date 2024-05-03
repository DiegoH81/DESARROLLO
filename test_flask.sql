-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-05-2024 a las 05:27:46
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `test_flask`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `nombre_producto` varchar(100) NOT NULL,
  `decripcion` varchar(100) NOT NULL,
  `precio` int(11) NOT NULL,
  `foto` varchar(100) NOT NULL,
  `status` int(11) NOT NULL,
  `id_comprador` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `id_usuario`, `nombre_producto`, `decripcion`, `precio`, `foto`, `status`, `id_comprador`) VALUES
(1, 1, 'Ps4', 'Consola de videojuegos', 1000, 'ps4.jpg', 1, 5),
(8, 1, 'Laptop', 'laptop', 5320, 'laptop.jpg', 1, 5),
(10, 8, 'Mouse', 'mouse', 180, 'dasdasdasdasfaf.jpg', 1, 6),
(11, 5, 'Mouse', 'mouse', 102, 'dasdadasdas.jpg', 1, 8),
(12, 1, 'Samsung Smart TV 65\" QLED 4K', 'Retroiluminación directa', 3999, 'tv.jpg', 1, 6),
(13, 4, 'Samsung Smart TV 85\" Crystal UHD', 'Colores realistas para que puedas ver todos los detalles. ', 5999, 'tv.jpg', 0, 0),
(14, 5, 'LG NanoCell 55\" NANO77 4K Smart TV', 'Amplia Gama de Colores: Nano Color. Procesado', 2131, 'tv2.jpg', 0, 0),
(15, 6, 'LG OLED 48\" A2 4K Smart TV con ThinQ AI', 'Amplia Gama de Colores: OLED Color.', 2399, 'tv2.jpg', 0, 0),
(16, 8, 'Televisor Philips 65\" 4K Ultra HD', 'Puerto Ethernet: Si. Resolución: UHD 4K. Alto: 90.8 cms. Ancho: 1.45 cms. ', 1799, 'tv_philips.jpg', 0, 0),
(17, 1, 'Iphone 15 Pro 128Gb', 'Peso: 0.187. Memoria interna: 128GB.', 5599, 'iphone15.jpg', 0, 0),
(18, 4, 'Celular Samsung Galaxy S23', 'Tipo de producto: Smartphone.', 4499, 's23.jpg', 0, 0),
(19, 5, 'Celular Xiaomi Redmi Note 13 Pro', 'Capacidad de almacenamiento: 8+256 GB. Tecnología celular: 4G. Procesador y generación: MediaTek Hel', 1249, 'xiaomi.jpg', 0, 0),
(20, 6, 'Celular Honor X7B 6.8\"', 'Capacidad de almacenamiento: 256GB. Tamaño pantalla celulares: 6.8\'. Tipo de batería: Li-ion Polymer', 799, 'honor.jpg', 0, 0),
(21, 8, 'Celular Huawei Nova 10 SE 6.67\"', 'Tamaño pantalla celulares: 6.67\'. Cámara frontal: 16 MP P. Cámara principal: 108 MP.', 900, 'nova.jpg', 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(64) NOT NULL,
  `user` varchar(64) NOT NULL,
  `password` varchar(64) NOT NULL,
  `email` varchar(64) NOT NULL,
  `foto` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `user`, `password`, `email`, `foto`) VALUES
(1, 'Diego Hidalgo', 'DiegoH', '123asdasd', 'diego@gmai.com', 'asdasd.png'),
(4, 'Leonardo Becerra', 'leo32914', 'leonardo32', 'leonardo@gmail.com', 'asd.jpg'),
(5, 'Joaquin Calderon', 'joaquin13', 'joaquin3211', 'joaquin@gmail.com', 'asd.jpg'),
(6, 'Jose Antonio', 'Jose1234', '12345678', 'jose@gmail.com', 'floopa.jpeg'),
(8, 'Sebastian Torres', 'SebastianTorres', 'sebastian12d1', 'sebastian@gmail.com', 'nah_id_win.jpg'),
(10, 'Anthony Huicho', 'anthony1971', 'anthony123', 'anthony@gmail.com', 'asd1.jpg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_productos_usuarios` (`id_usuario`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `fk_productos_usuarios` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
