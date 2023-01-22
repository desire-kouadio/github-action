## github-action

### Principe

- Le test unitaire est une méthode agile de travail qui consiste à tester des petites parties d’un code, que l’on appelle unités, de manière isolée. Les unités que l’on teste sont le plus souvent des fonctions et des classes mais la procédure de test peut s’appliquer sur des modules entiers.

- L’objectif des tests unitaires est donc de s’assurer que chaque élément constitutif du code est en bonne santé. Dans la pratique, on donne des entrées à l’unité et on vérifie que la sortie produite par l’unité correspond bien à ce qu’elle est censée renvoyer.

### Test unitaire vs Test d’intégration

- Alors que le test unitaire vérifie que toutes les unités du code fonctionnent indépendamment, le test d’intégration s’assure lui qu'elles fonctionnent ensemble. 
Les tests d'intégration sont axés sur des cas d’usage réels. Ils font ainsi souvent appel à des données externes comme des databases ou des serveurs web. Un test unitaire n’a quant à lui besoin que de données qui sont créées exclusivement pour le test. Il est donc beaucoup plus simple à implémenter.

### Exemple 

- Imaginez que l’on teste le fonctionnement d’un phare sur une voiture. Le test d’intégration vérifie que le phare s’allume lorsqu'on appuie sur le bon bouton. 
Les tests unitaires, s’assureront eux du bon fonctionnement de chaque élément du phare
pris séparément (fonctionnement du bouton, de la batterie, des câbles, des ampoules…).