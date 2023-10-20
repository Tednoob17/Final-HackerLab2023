#include <stdio.h>

char flag[] = {'C', 'T', 'F', '_', 'f', 'a', 'c', 'k', 'e', '_', 'f', 'l', 'a', 'g', '_', 'g', 'u', 'y', 's'};

int key[] = {}; // You need to find out the key
int new[sizeof(flag)];

void f(int t[], int len) {
    int *c = t;
    for (int i = 0; i < len; i++) {
        for (int j = i; j < len - 1; j++) {
            int temp = c[j];
            c[j] = c[j + 1];
            c[j + 1] = temp;
        }
    }
}

int main() {
    int len = sizeof(flag) / sizeof(flag[0]);
    for (int alt = 0; alt < len; alt++) {
        new[alt] = (flag[alt] << key[alt % (sizeof(key) / sizeof(key[0]))]) % 256;
    }
    f(new, len);

    for (int i = 0; i < len; i++) {
        printf("%d ", new[i]);
    }

    return 0;
}


// Output : 80, 248, 148, 40, 200, 64, 164, 248, 160, 248, 188, 32, 184, 144, 176, 152, 196, 192, 140, 230, 198, 230, 202, 216, 190, 202, 110, 144, 248, 56, 168, 24, 160, 144, 40, 8


