#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

void new_cmd(void);
void open_cmd(void);
void close_cmd(void);
void close_all_cmd(void);
void save_cmd(void);
void save_as_cmd(void);
void save_all_cmd(void);
void print_cmd(void);
void exit_cmd(void);

void run_cmd(const char *cmd);

struct {
    char *cmd_name;
    void (*cmd_pointer)(void);
} file_cmd[] = {
    {"new", new_cmd},
    {"open", open_cmd},
    {"close", close_cmd},
    {"close all", close_all_cmd},
    {"save", save_cmd},
    {"save as", save_as_cmd},
    {"save all", save_all_cmd},
    {"print", print_cmd},
    {"exit", exit_cmd}
};

int main(void)
{
    run_cmd("new");
    run_cmd("OPEN");
    return 0;
}


void run_cmd(const char *cmd)
{
    int cmd_cnt = sizeof(file_cmd)/sizeof(file_cmd[0]);
    char cmd_cpy[21], *p;

    strcpy(cmd_cpy, cmd);
    if (strlen(cmd) == 21) {
        cmd_cpy[20] = '\0';
    }

    for (p = cmd_cpy; *p != '\0'; p++)
    {
        *p = tolower(*p);
    }

    for (int i = 0; i < cmd_cnt; i++) {
        if (strcmp((file_cmd[i]).cmd_name, cmd_cpy) == 0) {
            return (file_cmd[i]).cmd_pointer();
        }
    }
}

void new_cmd(void)
{
    printf("new_cmd\n");
}
void open_cmd(void)
{
    printf("open_cmd\n");
}
void close_cmd(void)
{
    printf("close_cmd\n");
}
void close_all_cmd(void)
{
    printf("close_all_cmd\n");
}
void save_cmd(void)
{
    printf("save_cmd\n");
}
void save_as_cmd(void)
{
    printf("save_as_cmd\n");
}
void save_all_cmd(void)
{
    printf("save_all_cmd\n");
}
void print_cmd(void)
{
    printf("print_cmd\n");
}
void exit_cmd(void)
{
    printf("exit_cmd\n");
}