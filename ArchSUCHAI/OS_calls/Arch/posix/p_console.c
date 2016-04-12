
#include "p_console.h"

static unsigned char verbose_level = 3;

//
char con_buf[CON_BUF_WIDTH];
char con_buf_index;

char con_entry[CON_BUF_WIDTH];
char con_entry_index;
bool con_entry_flag; //true if a new attemp of command has arrived

char con_cmd[CON_BUF_WIDTH];
char con_cmd_index;

char con_args[CON_ARG_QTY][CON_ARG_WIDTH];

char con_arg_count;

bool con_arg_toolong;

char con_prev_char;

bool con_escape_flag;
bool con_arrow_flag;

char con_newchar;
bool con_init_flag;
bool con_active;

bool con_cmd_toolong_flag;

void con_init(void){
    unsigned char i;

    for(i = 0; i < CON_BUF_WIDTH; i++){
        con_buf[i] = '\0';
    }
    con_buf_index = 0;
    con_prev_char = 0;

    con_escape_flag = false;
    con_arrow_flag = false;

    con_init_flag = false;
    con_active = false;

    con_cmd_toolong_flag = false;

    return;
}

void con_cmd_from_entry(char *entry){}

ParsedInput con_cmd_handler(void){
    ParsedInput newPI;
//    DispCmd newCmd;
//    newCmd.idOrig = SCH_TCONSOLE_IDORIG;
//    newCmd.sysReq = CMD_SYSREQ_MIN;
//    newCmd.cmdId = CMD_CMDNULL;  /* cmdNULL */
//    newCmd.param = 0;

    if(con_entry_flag && con_entry_index > 0 )
    {
        con_cmd_from_entry(con_entry);
        if(con_arg_toolong)
        {
            newPI.cmdId = con_id_error_invalid_arg;
            newPI.param = 0;
            con_arg_toolong = false;
            con_entry_flag = false;

            return newPI;
        }
        
        /* ------------ EXECUTE GENERIC COMMAND ---------------*/
        if(strcmp(con_cmd, "exe_cmd") == 0)
        {
            int cmd, param;
            char* end;

            switch(con_arg_count)
            {
               case 2:
                  cmd=(unsigned int)strtoul(con_args[0], &end, 0);
                  param = atoi(con_args[1]);

                  newPI.cmdId = cmd;
                  newPI.param = param;        /* Argument to the command */
                  break;
              default:
                  newPI.cmdId = con_id_error_count_arg;  /* con_error_count_arg */
              break;
           }
           con_arg_toolong = false;
           con_entry_flag = false;
           return newPI;
        }

       /* ------ To get here the cmd has to fail all the comparisons  ------*/
       newPI.cmdId = con_id_error_unknown_cmd; /* con_error_unknown_cmd */

    }else
        if(con_cmd_toolong_flag){
            newPI.cmdId = con_id_error_cmd_toolong;

            con_cmd_toolong_flag = false;
        }

    con_arg_toolong = false;
    con_entry_flag = false;

    return newPI;
}


ParsedInput OSW_ConsoleInputParser(void){
    ParsedInput newPI;
    
    //printf(">> ");
    //int a = scanf(">> %s", con_cmd);
    char *ptr, *stat; long ret;
    stat = fgets(con_cmd, CON_BUF_WIDTH, stdin);
    if(stat == NULL){
        printf("OSW_ConsoleInputParser, invalid character \r\n");
        newPI.cmdId = 0;
        newPI.param = 0;
        return newPI;
    }
    else{        
        ret = strtol(con_cmd, &ptr, 16);
        //printf("OSW_ConsoleInputParser, ptr \"%c\" \r\n", *ptr);
        if(*ptr != ' '){
            printf("OSW_ConsoleInputParser, error parsing input arg1 %c \r\n", *ptr);
            newPI.cmdId = 0;
        }
        else{
            newPI.cmdId = ret;
            //printf("ret = 0x%04X \r\n", (unsigned int)ret);
        }
        
        ret = strtol(ptr, &ptr, 10);
        //printf("OSW_ConsoleInputParser, ptr \"%c\" \r\n", *ptr);
        if( *ptr != '\n' ){
            printf("OSW_ConsoleInputParser, error parsing input arg2 %c \r\n", *ptr);
            newPI.param = 0;
        }
        else{
            newPI.param = ret;
            //printf("ret = %04d \r\n", (int)ret);
        }
        
        return newPI;
    }
}
