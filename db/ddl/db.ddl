CREATE TABLE 'JPK_NAGLOWEK'
(
	'NAGLOWEK_ID' NUMERIC NOT NULL PRIMARY KEY,
	'CZAS_WYSLANIA' NUMERIC NOT NULL,
	'CZAS_UTWORZENIA' NUMERIC NOT NULL,
	'DATA_OD' NUMERIC NOT NULL,
	'DATA_DO' NUMERIC NULL,
	'ROKMC' NUMERIC NOT NULL
)
;

CREATE TABLE 'JPK_PODMIOT'
(
	'PODMIOT_ID' NUMERIC NOT NULL PRIMARY KEY,
	'NAGLOWEK_ID' NUMERIC NOT NULL,
	'NIP' TEXT NOT NULL,
	'IMIE' TEXT NOT NULL,
	'NAZWISKO' TEXT NOT NULL,
	'DATA_URODZENIA' NUMERIC NOT NULL,
	'TELEFON' NUMERIC NULL,
	CONSTRAINT 'FK_JPK_PODMIOT_JPK_NAGLOWEK' FOREIGN KEY ('NAGLOWEK_ID') REFERENCES 'JPK_NAGLOWEK' ('NAGLOWEK_ID') ON DELETE No Action ON UPDATE No Action
)
;

CREATE TABLE 'VAT_SPRZEDAZ'
(
	'SPRZEDAZ_ID' NUMERIC NOT NULL PRIMARY KEY,
	'NAGLOWEK_ID' NUMERIC NOT NULL,
	'NR_KONTRAHENTA' TEXT NOT NULL,
	'DOWOD_SPRZEDAZY' TEXT NOT NULL,
	'DATA_WYSTAWIENIA' NUMERIC NOT NULL,
	'DATA_SPRZEDAZY' NUMERIC NOT NULL,
	'P_6' NUMERIC NULL,
	'P_8' NUMERIC NULL,
	'P_9' NUMERIC NULL,
	'P_11' NUMERIC NULL,
	'P_13' NUMERIC NULL,
	'P_15' NUMERIC NULL,
	'P_16' NUMERIC NULL,
	'P_19' NUMERIC NULL,
	'P_96' NUMERIC NULL,
	CONSTRAINT 'FK_VAT_SPRZEDAZ_JPK_NAGLOWEK' FOREIGN KEY ('NAGLOWEK_ID') REFERENCES 'JPK_NAGLOWEK' ('NAGLOWEK_ID') ON DELETE No Action ON UPDATE No Action
)
;

CREATE TABLE 'VAT_ZAKUP'
(
	'ZAKUP_ID' NUMERIC NOT NULL PRIMARY KEY,
	'NAGLOWEK_ID' NUMERIC NOT NULL,
	'NR_DOSTAWCY' TEXT NOT NULL,
	'DOWOD_ZAKUPU' TEXT NOT NULL,
	'DATA_ZAKUPU' NUMERIC NOT NULL,
	'DATA_WPLYWU' NUMERIC NOT NULL,
	'P_61' NUMERIC NULL,
	'P_77' NUMERIC NULL,
	'P_78' NUMERIC NULL,
	CONSTRAINT 'FK_VAT_ZAKUP_JPK_NAGLOWEK' FOREIGN KEY ('NAGLOWEK_ID') REFERENCES 'JPK_NAGLOWEK' ('NAGLOWEK_ID') ON DELETE No Action ON UPDATE No Action
)
;