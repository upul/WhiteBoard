#include <iostream>
#include <vector>

namespace convutils
{
	using namespace std;

	class Im2Col
	{
	public:
		Im2Col();
		~Im2Col();
        
        vector<vector<double>> im2col(vector<vector<vector<vector<double>>>> images,
        	                           int filter_width,
        	                           int filter_height,
        	                           int padding_height,
        	                           int padding_width,
        	                           int stride_height,
        	                           int stride_widith
        	                           );
		

        vector<vector<vector<vector<double>>>> col2img(vector<vector<double>> im2col,
		                                                 int batch_size,
														 int n_channels,
														 int img_height,
														 int img_width,
														 int filter_height,
														 int filter_width,
														 int padding_height,
														 int padding_width,
														 int stride_height,
														 int stride_widith);


        vector<vector<vector<vector<double>>>> pad(vector<vector<vector<vector<double>>>> images,
	                                              int padding_height, 
	                                              int padding_width);
    };

};

    
