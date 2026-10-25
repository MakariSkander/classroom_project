

#include <iostream>
#include<vector>
#include<string>
using namespace std;


vector<char> Encode(char u)
{    
    vector<char> Code;
    Code.resize(8);
    // mélange aleatoire des indices entre 0 et 7 afin de mélanger les lettres
    char T[8];
    for (int t = 0; t < 8; t++) T[t] = t;
    for (int i = 0; i < 7; i++)
    {
        int n = (rand() * 7) / RAND_MAX; // tirage entre 0 et 7
        int a = T[n];
        T[n] = T[i];
        T[i] = a;
    }
    for (int i = 7; i >= 0; i--)
    {
        int r = (rand() * 18) / RAND_MAX + 8; // tirage aléatoire
        if ((u >> i) & 1) Code[T[i]] = 'a' + 7 - i; // lettre entre a et h;
        else Code[T[i]] = r + 'a'; // lettre aleatoire entre i et z;
    }
    return Code;
}

void AfficheCodege(vector <vector<char> >Vectlocale) {
    vector<char> v;
    for (int i = 0;i < Vectlocale.size();i++) {
        v = Vectlocale[i];
        for (int j = 0;j < v.size();j++) cout << v[j];
        cout << " ";
    }
 
    cout << endl;
}

void Histogramme(vector<char> chaine, int* Histo) {
    if (Histo == NULL)return;
    for (int i = 0;i < 26;i++) Histo[i] = 0;
    for (int i = 0;i < chaine.size();i++) {
        int indice = chaine[i] - 'a';
        if (indice < 26 && indice>=0) Histo[indice]++;
    }
}
char Decode(vector <char> vect) 
{
    int Histo[26];
    char resultat = 0;
    Histogramme(vect, Histo);
    for (int i = 0;i < 8;i++) 
    {
        if (Histo[i] != 0)
            resultat = resultat + (1 << (7 - i));// cette methode de decalage et le mem que// power(2,7-i);
       
    }
    return resultat;
}
vector<char>DecodeGroupe(vector<vector<char>>VectGlobal) 
{
    vector<char> Vectres;
    for (int i = 0;i < VectGlobal.size();i++) 
    {
        vector <char> vect = VectGlobal[i];
        char r;
        r = Decode(vect);
        Vectres.push_back(r);
    }
    return Vectres;
}

int main()
{
    vector<char> vect;
   
    string example = "Bonjour";
    vector <vector<char> >VectGlobal;
    for (int i = 0; i <example.length(); i++)
    {
        vect = Encode(example[i]);
        VectGlobal.push_back(vect);
    }
    AfficheCodege(VectGlobal);



    vect = Encode('a');

    for (int i = 0; i < vect.size(); i++)
        cout << vect[i];
    cout << endl;

    char r;
    r = Decode(vect);
    cout << "le charactere decoder = " << r << endl;

    vector <char>Resultat;
    Resultat = DecodeGroupe(VectGlobal);
    for (int i = 0;i < Resultat.size();i++)cout << Resultat[i];
    cout <<endl<< "fin" << endl;
}
