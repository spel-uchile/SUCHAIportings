
#if(SCH_TARGET_ARCH == 0)
    #include "../Arch/posix/p_queue.h"
#elif(SCH_TARGET_ARCH == 1)
    #include "../Arch/freertos/include/p_queue.h"
#endif
