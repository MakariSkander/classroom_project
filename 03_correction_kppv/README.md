# 📍 KNN Classification (KPPV)

Windows desktop application in C++ (MFC) that shows how the **k-nearest neighbors** algorithm (KNN, *k plus proches voisins* in French) classifies points.

## How to use

| Action | Result |
|---|---|
| **Left click** | Adds a training point of class 0 |
| **Right click** | Adds a training point of class 1 |
| **Middle click** | Classifies the clicked point with KNN (k = 7). Blue = class 0, red = class 1 |
| **Valider button** | Displays all training points (squares = class 1, circles = class 0) |
| **Barycentre button** | Computes and draws the barycenter (center) of each class |

## How it works

For a new point, the program computes the Euclidean distance to every training point, sorts the distances, and takes a majority vote among the 7 nearest neighbors.

## Tech

- C++
- MFC (Microsoft Foundation Classes)
- Microsoft Visual Studio

## Run

Open `Correction de Kppv.sln` in Visual Studio (with the MFC component installed), then build and run.
