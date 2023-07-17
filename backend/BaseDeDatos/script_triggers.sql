-- FUNCION QUE ACTUALIZA LA CANTIDAD DE DIAS QUE TIENE UNA VIGILANCIA
CREATE OR REPLACE FUNCTION update_cant_dias(vigilancia INTEGER,  estado BOOLEAN)
RETURNS void AS $$
DECLARE 
	dias INTEGER;
BEGIN
	SELECT v.cant_dias INTO dias FROM public."Vigilancia_vigilancia" AS v WHERE v.id = vigilancia;
	IF estado = TRUE THEN
		dias := dias + 1;
		UPDATE "Vigilancia_vigilancia" SET cant_dias = dias WHERE id = vigilancia;
	ELSE
		dias := dias - 1;
		UPDATE "Vigilancia_vigilancia" SET cant_dias = dias WHERE id = vigilancia;
	END IF;
END;
$$ LANGUAGE plpgsql;



-- FUNCION QUE EJECUTA EL TRIGGER 'tr_aumentar_cant_dias'
CREATE OR REPLACE FUNCTION aumentar_cant_dias_func() 
RETURNS TRIGGER AS $$
BEGIN
    PERFORM update_cant_dias(NEW.fk_vigilancia_id::INTEGER, TRUE);
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- TRIGGER QUE SE EJECUTA AL CREAR UN NUEVO DIA DE VIGILANCIA
CREATE TRIGGER tr_aumentar_cant_dias
AFTER INSERT
ON public."Vigilancia_diasvigilancia"
FOR EACH ROW
EXECUTE FUNCTION aumentar_cant_dias_func();




-- FUNCION QUE EJECUTA EL TRIGGER 'tr_disminuir_cant_dias'
CREATE OR REPLACE FUNCTION disminuir_cant_dias_func() 
RETURNS TRIGGER AS $$
BEGIN
    PERFORM update_cant_dias(OLD.fk_vigilancia_id::INTEGER, FALSE);
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- TRIGGER QUE SE EJECUTA AL ELIMINAR UN DIA DE VIGILANCIA
CREATE TRIGGER tr_disminuir_cant_dias
AFTER DELETE
ON public."Vigilancia_diasvigilancia"
FOR EACH ROW
EXECUTE FUNCTION disminuir_cant_dias_func();





-- prueba de triggers

-- INSERT INTO public."Vigilancia_diasvigilancia" 
-- 	(dia,hora_inicio,hora_fin,turno,dia_completo,fk_personal_id,fk_vigilancia_id)
-- 	VALUES ('2023-03-31', NULL, NULL, NULL, TRUE, DEFAULT,1)
	
-- DELETE FROM public."Vigilancia_diasvigilancia" WHERE id=13;

-- UPDATE public."Vigilancia_vigilancia" SET cant_dias = 0 WHERE id=1;



-- DROP TRIGGER tr_aumentar_cant_dias on public."Vigilancia_diasvigilancia";
-- DROP TRIGGER tr_disminuir_cant_dias on public."Vigilancia_diasvigilancia";
-- DROP FUNCTION aumentar_cant_dias_func;
-- DROP FUNCTION disminuir_cant_dias_func;

-- DROP FUNCTION update_cant_dias;