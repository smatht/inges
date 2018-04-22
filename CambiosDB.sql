-- Editado por: Matias G. Sticchi (21 abr 2018 21:04)

--Se realizo una super migracion.
--Se cambio TipoMovCaja de fondos a mantenimiento para evitar referencia cruzada.

--Migracion fodos 022_auto_20180421_1759:
--Se cambia el nombre de tabla fondos_tipomovcaja por mantenimiento_tipomovcaja

--Migracion mantenimiento 012_tipomovcaja:
--Se actualizan ContentTypes. Se crea el nuevo modelo en mantenimiento y se lo asocia a la tabla renombrada

--Migracion fondos 0023_auto_20180421_1930:
--Se agrega foreign key de Tipomovcaja a mantenimiento.TipoMovCaja. Se elimina modelo TipoMovCaja

-- Si genera error hay que corregir la tabla ContentType
select * from public.django_content_type -- Tiene que haber solo un model label de cada modelo, si hay mas
delete from public.auth_permission where content_type_id=61 -- Primero se lo borra de auth
delete from public.django_content_type where id=61 -- despues de contentType

