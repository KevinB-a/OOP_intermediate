Exercice 3
: Les méthodes magiques
Dans cet exercice nous allons simuler quelques comportements d’objets que nous pourrions 
retrouver dans la gestion d’un magasin.
Votre programme sera composé de deux classes principales
: Customer et Employee. Toutes deux 
héritent d’une classe commune Person.
La classe personne définit les attributs nom, prénom et âge qui sont communs à la fois au client et à 
l’employé.
La classe client a comme attributs spécifiques un panier, vide par défaut, qui pourra contenir les 
produits que le client achète et un attribut avec le montant total à payer lors de son passage en 
caisse. Ce montant est mis à jour à chaque fois qu’un produit est ajouté au panier.
La classe employé possède quant à elle un attribut particulier, le statut du salarié. Par défaut celui-ci
est employé. Les statuts possibles sont
:  employé, technicien, manager et cadre par ordre de 
hiérarchie.
Vous aurez également besoin de créer une classe Product qui représente les produits du magasin. 
Elle possède les attributs prix et nom du produit