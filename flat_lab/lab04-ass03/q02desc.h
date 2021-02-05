#define NoSt 4
#define NoIn 2
#define NoFst 1

int state[NoSt] = {0, 1, 2, 3};
int input[NoIn] = {0, 1};
int Rules[][NoIn] = {{1, 3}, {0, 2}, {3, 1}, {2, 0}};

int Final_st[NoFst] = {0};
int Initial_st = 0;