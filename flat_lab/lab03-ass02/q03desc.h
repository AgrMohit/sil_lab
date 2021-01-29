// starts with 0 - even length
// starts with 1 - odd length
#define NoSt 5
#define NoIn 2
#define NoFst 2

int state[NoSt] = {0, 1, 2, 3, 4};
int input[NoIn] = {0, 1};
int Rules[][NoIn] = {{1, 3}, {2, 2}, {1, 1}, {4, 4}, {3, 3}};
int Final_st[NoFst] = {2, 3};
int Initial_st = 0;
