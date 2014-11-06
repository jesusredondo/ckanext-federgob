ckanext-federgob
========================


## ¿Qué es FederGob?

Es una extensión para CKAN que facilita el proceso de federación con [Datos.gob.es](http://www.datos.gob.es/), el catálogo de datos oficial de España.

La documentación oficial para federar portales contra [Datos.gob.es](http://www.datos.gob.es/) es la siguiente: [manual del Federador](http://www.datos.gob.es/content/manual-de-uso-de-herramienta-federador). Es recomendable leer la documentación oficial sobre cómo se deben estructurar los metadatos: [Norma Técnica de Interoperabilidad de Reutilización de Recursos de Información](https://www.boe.es/buscar/doc.php?id=BOE-A-2013-2380).

Esta extensión sólo permite la federación mediante metadatos representados en RDF. Se modifican los metadatos originales proporcionados por CKAN para adecuarlos a la Norma Técnica de Interoperabilidad mencionada anteriormente.

El vocabulario principal para describir los metadatos es [DCAT](http://www.w3.org/TR/vocab-dcat/). [Datos.gob.es](http://www.datos.gob.es/) ofrece un [manual](http://datos.gob.es/sites/default/files/federador_-_manual_de_usuario.pdf) que incluye una plantilla rdf/xml que es utilizada como esqueleto para este plugin. 

Es recomendable revisar [esta presentación sobre el Federador](http://www.w3.org/2013/share-psi/wiki/images/8/89/Share-PSI_FederationTool_v01_en_paper.pdf) y el [manual del usuario](http://datos.gob.es/sites/default/files/federador_-_manual_de_usuario.pdf) para aprender cómo utilizar el Federador.


## ¿Cómo funciona?

Por defecto CKAN genera metadatos en rdf/xml de cada dataset utilizando el vocabulario DCAT. 

FederGob adecúa estos metadatos a los que consume el Federador de [Datos.gob.es](http://www.datos.gob.es/) (ver el anexo I en el [manual del usuario del Federador]([http://datos.gob.es/sites/default/files/federador_-_manual_de_usuario_2.docx])). Además, se crean metadatos sobre el propio portal, necesarios para completar el proceso de federación.

FederGob incluye scripts para automatizar la generación de los metadatos periódicamente.


## Prerrequisitos

1. La versión CKAN del catálogo en el que se instale el plugin debe ser la 2.0 o superior (no se ha testeado con versiones anteriores).

2. Todos los datasets del catálogo CKAN deben tener el campo etiqueta (tag) relleno con uno de los valores que aparecen en la segunda columna de la primera tabla del anexo IV en la [Norma Técnica de Interoperabilidad de Reutilización de Recursos de Información](https://www.boe.es/buscar/doc.php?id=BOE-A-2013-2380).

3. Todos los datasets deben tener el campo licencia relleno. En el caso de que no esté relleno se tomará la licencia [Creative Commons Attribution](http://www.opendefinition.org/licenses/cc-by) por defecto.

4. La primera frase de la descripción de cada dataset (todo lo que se encuentre antes del primer punto ".") se utilizará para rellenar el campo dcat:description. Por lo tanto sería recomendable que esta primera línea se utilice para describir el dataset brevemente. 


## Limitaciones

1. No soporta descripciones multi-valuadas. (Por ejemplo, descripciones en varios idiomas).

2. Este plugin no se ha testeado en conjunto con [ckanext-dcat](https://github.com/ckan/ckanext-dcat), podría haber problemas si ambos estuvieran funcionando al unísono.
 

## ¿Cómo instalar el FederGob?

Copia el [plugin](https://github.com/jesusredondo/ckanext-federgob) a tu carpeta `src` (normalmente es: /usr/lib/ckan/default/src/).

Instalar el plugin:

    cd ckanext-federgob
    sudo python setup.py develop

Asegurarse que `federgob está en la lista de plugins activos del fichero de configuración de CKAN y reiniciar Apache.


## ¿Cómo configurar FederGob?

FederGob tiene que ser configurado en local para que cree los metadatos. Después el Federator [Datos.gob.es](http://www.datos.gob.es/) se encargará de leer la información generada.

Si tienes problemas con la instalación, por favor crea un nuevo issue en el repositorio.


### Configuración local

Estos pasos permiten configurar la generación de los metadatos periódicamente. Todos los comandos tienen que correrse en la ruta: `.../ckanext-federgob/ckanext/federgob/FDG/`.


#### Configurar los metadatos del portal

Para configurar los metadatos del portal hay que ejecutar el script `config.py` → `sudo python config.py`. Hay que rellenar los siguientes campos:

1. **{-URL-CATALOG-}** : Es la URL del catálogo. Por ejemplo: `http://opendata.caceres.es`.

2. **{-URL-DATASET-}** : Es la URL base donde se encuentran todos los datasets. Normalmente esta URL toma la forma: **{-URL-CATALOG-}**/dataset. Por ejemplo: `http://opendata.caceres.es/dataset`. Otro ejemplo sería `http://datahub.io/dataset` para `http://datahub.io`.

3. **{-LANGUAGE-}** : Idioma del catálogo. Tiene que seguir el estándar RFC 1766. Por ejemplo: `es`, `en` o `fr`.

4. **{-TITLE-}** : Título del catálogo. Ejemplo: `Opendata Cáceres`.

5. **{-DESCRIPTION-}** : Descripción pormenorizada del catálogo.

6. {-ISSUED-} : Fecha en la que se creó el catálogo, se debe utilizar el estándar [ISO-8601](http://www.w3.org/TR/NOTE-datetime). Por ejemplo: `2014-07-02T10:45:15`.

7. **{-URL-PUBLISHER-}** : URL de la organización que publica los datos en el catálogo. Tiene que ser una URL que siga el formato establecido por el NTI. Para más información consultar el anexo II C del [manual del Federador](http://datos.gob.es/sites/default/files/federador_-_manual_de_usuario_2.docx). Por ejemplo: `http://datos.gob.es/recurso/sector-publico/org/Organismo/L01100377`.

8. **{-URL-LICENSE-}** : URL de la página web donde se describen los términos de usos del catálogo. Por ejemplo: `http://opendata.caceres.es/terminos`.

Si se edita manualmente el fichero `fields.conf` en lugar de utilizar el script `config.py` debes ejecutar `merge_metadata.py` → `sudo python merge_metadata.py` para que los cambios se hagan efectivos. 

Se puede comprobar que la configuración ha sido correcta ejecutando el script que genera los metadatos: `federatedatosgob.py` →  `sudo python federatedatosgob.py`. Si todo ha sido satisfactorio, todos los datasets del catálogo se mostrarán por pantalla y se podrá acceder al fichero de metadatos en la URL: **{-URL-CATALOG-}**/federator.rdf .

#### Automatizar la actualización

Como se ha visto en el punto anterior, los metadatos se generan cada vez que se ejecuta el script `federatedatosgob.py`. Para automatizar la generación de metadatos se debe ejecutar periódicamente el script `federatedatosgob.py`. Se puede hacer uso de [Cron](http://unixhelp.ed.ac.uk/CGI/man-cgi?crontab+5) en Linux para planificar tareas periódicamente, se recomienda que se configure [Cron](http://unixhelp.ed.ac.uk/CGI/man-cgi?crontab+5) para que se ejecute `federatedatosgob.py` según las necesidades de actualización de cada portal.

Adicionalmente, FederGob incluye un script que configura [Cron](http://unixhelp.ed.ac.uk/CGI/man-cgi?crontab+5)  por defecto para que `federatedatosgob.py` se ejecute cada día a las 00.00 a.m. Simplemente hay que ejecutar `auto_crontab.py` como root → `sudo python auto_crontab.py` para establecer la actualización diaria a las 00.00 a.m.

### Configuración externa: Configurar el Federador del portal Datos.gob.es

El federador debe leer los metadatos generados en la URL: {-URL-CATALOG-}/federator.rdf. Sigue el [manual oficial del Federador de Datos.gob.es](http://www.datos.gob.es/content/manual-de-uso-de-herramienta-federador) para configurarlo.


## Reconocimientos
Este plugin ha sido desarrollado por el grupo [Quercus SEG](http://www.unex.es/investigacion/grupos/quercus) para federar el portal [Opendata Cáceres](http://opendata.caceres.es/) portal.

## Licencia
Este plugin se publica bajo la licencia [GNU Affero General Public License (AGPL) v3.0](http://www.gnu.org/licenses/agpl-3.0.html)

