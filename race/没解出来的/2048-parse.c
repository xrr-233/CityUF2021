int parse(int grid[][4], unsigned char* buf)
{
	for (int i = 0 ;i < 16; i++){
		int sig = 0;
		while (!sig){
			switch (*buf)
			{
				case 0x10:
				// pos add operand
					buf += *(buf+1);
					break;
				case 0x20:
				// pos sub operand
					buf -= *(buf+1);
					break;
				case 0x30:
				// retrieve the value
					if ((((grid[i/4][i%4]>>8)^0xa5) != *(buf+1)) || (grid[i/4][i%4]&0xff^0xa6) != *(buf+2))
						return 0;
					sig = 1;
					buf+=3;
					break;
				default:
					return 0;
			}
		}
	}
	return 1;

}
