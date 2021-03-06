# Guide pratique de l'anonymisation

L'anonymisation est un processus mis en oeuvre lors de certains traitements de données personnelles. Il vise, dans un jeu de donné publié, à empêcher de:

* Distinguer un individu.
* Lier des informations relatives à un individu.
* Inférer des informations concernant un individu.

L'anonymisation ne se limite pas à la suppression des champs identifiants d'un jeu de données, comme le nom ou l'adresse d'un individu. D'autres variables, qualifiées de réidentifiantes, peuvent être utilisées pour identifier un individu au sein d'un jeu de données. Il est donc nécessaire de mettre en oeuvre des techniques plus avancées d'anonymisation, comme la généralisation.

## Classement des variables

Une des première étapes du processus d'anonymisation consiste à classer les variables en 3 catégories:

* **Variables (directement) identifiantes** : nom, prénom, identifiant utilisateur, numéro de Sécurité Sociale, etc.
* **Variables quasi-identifiantes** : une variable est quasi-identifiante, si, une fois combinée avec d'autres variables, elle permet l'identification d'un individu. Exemple : l'identité de vos parents et votre âge.
* **Variables sensibles** : une variable est dite sensible si elle révèle une information personnelle, privée ou confidentielle à propos d'un individu. Exemple : la personne est malade ou non.  
Notons que la frontière entre ces différents types est parfois assez poreuse : on peut tout à la fois considérer l'adresse d'un individu comme une variable identifiante, quasi-identifiante et sensible. 

## Variables identifiantes

Les variables identifiantes sont obfusquées ou tout simplement retirées lors de l'anonymisation.
On parle alors de **pseudonymisation** une fois cette étape passée. Le jeu de données n'est à ce stade pas encore anonymisé.

### Obfuscation

Parfois, certaines variables identifiantes ne doivent pas être retirées du jeu de données anonymisé. C'est par exemple le cas lorsque le jeu données servira à analyser des parcours utilisateur et qu'un identifiant individuel apparaitra plusieurs fois dans le jeu de données anonymisé. Il convient alors d'obfusquer cet identifiant pour ne pas le dévoiler tout en préservant son caractère particulier.

La méthode retenue dans ce cas est celle du hachage des champs concernés. Les champs concernés doivent être hachés en utilisant un algorithme issu de la famille SHA-2 ou SHA-3 http://csrc.nist.gov/publications/fips/fips180-4/fips-180-4.pdf, les plus robustes à l'heure actuelle. Ces fonctions sont disponibles dans toutes les blibliothèques cryptographiques des langages de programmation.

R: digest
Python: hashlib
SAS
Java


## Anonymisation par généralisation

Lors d'une anonymisation par aggrégation, les variables sont modifiées de telle sorte à rendre la ré-identification impossible. Ces modifications peuvent prendre plusieurs formes.  
+ On peut appliquer un changement d'échelle, en passant, par exemple, d'un code communal (75001) à un code départemental (75).  
+ On peut aussi fusionner plusieurs modalités, soit de façon générale (sur toute la base), soit de manière locale (seules les modalités des lignes qui posent problème seront modifiées). Exemple : deux lignes qui prennent comme code postal "75001" et "75014" prennent comme nouvelle modalité "75001 ou 75014".

### K-anonymat
On considère qu'une base de données est k-anonymisée, si et seulement si à chaque combinaison de modalités de variables quasi-identifiantes qui composent la base correspond un *minimum* de k d'individus.

### L-Diversité
On considère qu'une base de données est l-diverse :
+ si à chaque combinaison de modalités de variables quasi-identifiantes qui composent la base correspond un groupe composé *d'au moins* k individus et,
+ si ce groupe présente *au moins* l modalités différentes en ce qui concerne la (ou les) variable(s) sensible(s).

### Mesurer la perte d'informations

ARTICLE 29 DATA PROTECTION WORKING PARTY
http://ec.europa.eu/justice/data-protection/article-29/documentation/opinion-recommendation/files/2014/wp216_en.pdf
