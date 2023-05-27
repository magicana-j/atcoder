#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool isSimilar(char a, char b) {
    char similar_characters[4][2] = {
        {'0', 'o'}, {'1', 'l'}, {'2', 'z'}, {'5', 's'}};

    for (int i = 0; i < 4; i++) {
        if (find(similar_characters[i][0], similar_characters[i][1], a)) }
}

int main(void) {
    int n;
    cin >> n;
    string s, t;
    cin >> s >> t;
    if (s.length() != n || t.length() != n) cout << "No" << endl;

    for (int i = 0; i < n; i++) {
    }
    return 0;
}
