data<- read.csv('HR_comma_sep.csv')
data2 <- data
dim(data2)
summary(data2)
str(data2)
data2$sales <- as.factor(data2$sales)
data2$salary <- as.factor(data2$salary)
data2$sales <- as.numeric(data2$sales)
data2$salary <- as.numeric(data2$salary)
str(data2)
#Standardiser les donnees
data2_standardize <- as.data.frame(scale(data2[1:10]))
data2_standardize
#Calculer la matrice de correlation
data2.mat <- as.matrix(data2_standardize)
#afficher la matrice de correlation
data2.mat 
#la matrice de covariance
cov.mat <- cor(data2_standardize) 
# afficher la matrice de covariance
cov.mat 
#tracer de la matrice de covariance pour identifier la correlation entre les caracteristiques
library(corrplot)
corrplot(cov.mat,method = 'color')
#Tracez la visualisation appropriée après avoir réduit la dimension de nos données.

#Valeurs propres / Variances
library("factoextra")
eig.val <- get_eigenvalue(res.pca)
eig.val

#La somme de toutes les valeurs propres donne une variance totale de 10.
#Dans notre analyse, les cinq premières composantes principales expliquent 64% de la variation.
#C'est un pourcentage acceptable.

var <- get_pca_var(res.pca)
var
# Coordonnées
head(var$coord)
# Cos2: qualité de répresentation
head(var$cos2)
# Contributions aux composantes principales
head(var$contrib)

# Coordonnées des variables
head(var$coord, 4)
fviz_pca_var(res.pca, col.var = "black")

ind <- get_pca_ind(res.pca)
ind
# Coordonnées des individus
head(ind$coord)
# Qualité des individus
head(ind$cos2)
# Contributions des individus
head(ind$contrib)
fviz_pca_ind (res.pca, pointsize = "cos2",
              pointshape = 21, fill = "#E7B800",
              repel = TRUE # Évite le chevauchement de texte
              )
