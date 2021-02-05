#define NoSt 4
#define NoIn 2
#define NoFst 1

int state[NoSt] = {0, 1, 2, 3};
int input[NoIn] = {0, 1};
int Rules[][NoIn] = {{1, 2}, {1, 1}, {3, 2}, {3, 2}};

int Final_st[NoFst] = {3};
int Initial_st = 0;