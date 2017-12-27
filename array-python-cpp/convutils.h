#include <iostream>
#include <vector>

namespace utils {
    using namespace std;

    class Im2Col {
    public:
        Im2Col();

        ~Im2Col();

        vector<vector<double>> im2col(const vector<vector<vector<vector<double>>>> images,
                                      const int filter_width,
                                      const int filter_height,
                                      const int padding_height,
                                      const int padding_width,
                                      const int stride_height,
                                      const int stride_width
        );


        vector<vector<vector<vector<double>>>> col2img(const vector<vector<double>> im2col,
                                                       const int batch_size,
                                                       const int n_channels,
                                                       const int img_height,
                                                       const int img_width,
                                                       const int filter_height,
                                                       const int filter_width,
                                                       const int padding_height,
                                                       const int padding_width,
                                                       const int stride_height,
                                                       const int stride_widith);


        vector<vector<vector<vector<double>>>> pad(const vector<vector<vector<vector<double>>>> images,
                                                   const int padding_height,
                                                   const int padding_width);
    };

};

    
