ckanext-federatedatosgob
========================


## What is federatedatosgob?

It is an extension for CKAN that eases the federation process of CKAN catalogs with the global catalog of Spain, [Datos.gob](http://www.datos.gob.es/).

The official documentation to federate portals against [Datos.gob](http://www.datos.gob.es/) can be found here: [Federator manual](http://www.datos.gob.es/content/manual-de-uso-de-herramienta-federador). It’s recommendable to read the official document about how metadata should structure: [Norma Técnica de Interoperabilidad de Reutilización de Recursos de Información](https://www.boe.es/buscar/doc.php?id=BOE-A-2013-2380).

This extension only supports RDF based federation. The original metadata created by CKAN is modified by this script, adapting it to the Norma Técnica de Interoperabilidad mentioned before. 

The main vocabulary to describe metadata is [DCAT](http://www.w3.org/TR/vocab-dcat/). [Datos.gob](http://www.datos.gob.es/) provides a [manual](http://datos.gob.es/sites/default/files/federador_-_manual_de_usuario.pdf) that includes a rdf/xml metadata template that is used as squeleton by this plugin. 

It is desirable to check [this presentation about Federator](http://www.w3.org/2013/share-psi/wiki/images/8/89/Share-PSI_FederationTool_v01_en_paper.pdf) and the [user manual](http://datos.gob.es/sites/default/files/federador_-_manual_de_usuario.pdf) to learn how to set up the Federator.


## How does it work?

By default CKAN generates rdf/xml metadata about every single dataset using DCAT vocabulary. 

Federatedatosgob adequates this metadata to the Federator template (see annex I in the [Federator user manual]([http://datos.gob.es/sites/default/files/federador_-_manual_de_usuario_2.docx])). Additionally, metadata about the catalog and the portal is created, completing the metadata needed for the federation. 

Federatedatosgob provides scripts to update the metadata periodically.


## Prerequisites

1. The CKAN version running the extension should be 2.0 or superior (hasn’t been tested with older versions).
All the datasets in the CKAN catalog should have filled the tag field (etiqueta) using one of the values that appear in the second column of first table of the Anexo IV in the [Norma Técnica de Interoperabilidad de Reutilización de Recursos de Información](https://www.boe.es/buscar/doc.php?id=BOE-A-2013-2380).

2. All the datasets must have a license in their license field, if not filled, the license [Creative Commons Attribution](http://www.opendefinition.org/licenses/cc-by) is taken by default.

3. The first sentence of each dataset description (everything before the first “.”) is used to fill the de metadata field “dcat:description”. So it would be a good idea to describe concisely the dataset in that first line. 


##Limitations

1. It doesn’t support multi-valued fields for descriptions.

2. This plugin has not been tested while using [ckanext-dcat](https://github.com/ckan/ckanext-dcat). Malfunctions could arise when both working.
 

## How to install federatedatosgob?

Copy the [plugin](https://github.com/jesusredondo/ckanext-federatedatosgob) to your ckan src folder (normally /usr/lib/ckan/default/src/).

Install the plugin:

    cd ckanext-federatedatosgob
    sudo python setup.py develop

Make sure to add federatedatosgob to ckan.plugins in your config file.


## How to configure federatedatosgob with the Federator?

Federatedatosgob must to be configured locally to create the metadata. Later, the Federator will read the metadata generated. 

If you have problems with the installation, please create a new issue.


### Local configuration

These steps have to be completed to configure the creation of the metadata periodically.
All commands must be run in the `.../ckanext-federatedatosgob/ckanext/federatedatosgob/FDG/` path.


#### Configure portal metadata

Run the `config.py` script → `sudo python config.py` to configure the metadata of your portal. The fields that must be completed are:

1. **{-URL-CATALOG-}** :  URL of the CKAN instance. Example: `http://opendata.caceres.es`.

2. **{-URL-DATASET-}** : URL base of all datasets. Usually is the value is: **{-URL-CATALOG-}**/dataset. For example: `http://opendata.caceres.es/dataset`, another example would be `http://datahub.io/dataset` for `http://datahub.io`.

3. **{-LANGUAGE-}** : Language of the whole catalog. It has to follow the RFC 1766 standard. Example value: `es`, `en` or `fr`.

4. **{-TITLE-}** : Title of the catalog. Example: `Opendata Cáceres`.

5. **{-DESCRIPTION-}** : Long textual description of the catalog.

6. {-ISSUED-} :  Date when the catalog was created in [ISO-8601 standard](http://www.w3.org/TR/NOTE-datetime). Example: `2014-07-02T10:45:15`.

7. **{-URL-PUBLISHER-}** : URL of the publishing organization.It has to follow the format established by the NTI. Check annex II C in the [Federator user manual](http://datos.gob.es/sites/default/files/federador_-_manual_de_usuario_2.docx). Example: `http://datos.gob.es/recurso/sector-publico/org/Organismo/L01100377`.

8. **{-URL-LICENSE-}** : Link to the web page that describes the terms of use of the catalog. Example: `http://opendata.caceres.es/terminos`.

If you manually edit the file `fields.conf` instead of using the script `config.py` you must run `merge_metadata.py` → `sudo python merge_metadata.py` to update the changes. 

To test the metadata generation, run `federatedatosgob.py` →  `sudo python federatedatosgob.py`. If everything works fine, all the datasets in the catalog should be displayed and the metadata could be accessed in the url: **{-URL-CATALOG-}**/federator.rdf .

#### Automatic updates

As we have seen before, the metadata is generated each time `federatedatosgob.py` is run. To automate the update, `federatedatosgob.py` must be run periodically. [Cron](http://unixhelp.ed.ac.uk/CGI/man-cgi?crontab+5) can be used to run tasks in given intervals or at a given time, you should configure it to your updating preferences.

Additionally, federatedatosgob includes a default method to configure [Cron](http://unixhelp.ed.ac.uk/CGI/man-cgi?crontab+5) each day at 00.00 a.m. To do so, simply run the script `auto_crontab.py` as root → `sudo python auto_crontab.py`.

### External configuration: Configure Federator from Datos.gob

The federator must read the metadata that is generated in the url: {-URL-CATALOG-}/federator.rdf. Follow the tutorials from datos.gob to set it up.


## Acknowledgements
This plugin has been developed by [Quercus SEG](http://www.unex.es/investigacion/grupos/quercus) to federate the [Opendata Cáceres](http://opendata.caceres.es/) portal.

## License
This plugin is published under the [GNU Affero General Public License (AGPL) v3.0](http://www.gnu.org/licenses/agpl-3.0.html)
