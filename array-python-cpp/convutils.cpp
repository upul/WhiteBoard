#include "convutils.h"
#include <random> 
using namespace convutils;

Im2Col::Im2Col()
{
}

Im2Col::~Im2Col()
{
}

vector<vector<double> > Im2Col::im2col(vector<vector<vector<vector<double> > > > images,
        	                           int filter_width,
        	                           int filter_height,
        	                           int padding_height,
        	                           int padding_width,
        	                           int stride_height,
        	                           int stride_widith
        	                           )
{
	int batch_size = images.size();
	int n_channels = images[0].size();
	int img_height = images[0][0].size();
	int img_width = images[0][0][0].size();   
    

    int new_width = int(img_width - filter_width + 2*padding_width) + 1;
    int new_height = int(img_height - filter_height + 2*padding_height) + 1;

    int col_height = filter_height*filter_width*n_channels;
    int col_width = batch_size*new_height*new_width;

    vector<vector<double> > result(col_height, vector<double>(col_width, 0.0));
	
    
	vector<vector<vector<vector<double> > > > padded_images;
	if(padding_height > 0 || padding_width > 0){
		padded_images = pad(images, padding_height, padding_width);
	}else{
		padded_images = images;
	}
        

    int itr = 0;
    for(int h=0; h<new_height; h++){
    	for(int w=0; w<new_width; w++){
    		for(int b=0; b<batch_size; b++){
    			int start_h = h*stride_height;
    			int end_h = h*stride_height + filter_height;
    			int start_w = w*stride_widith;
    			int end_w = w*stride_widith + filter_width;

    			int k=0;
    			for(int c=0; c<n_channels; c++){
    				for(int i=start_h; i<end_h; i++){
                        for(int j=start_w; j<end_w; j++){
                        	result.at(k).at(itr) = padded_images.at(b).at(c).at(i).at(j);
                        	k += 1;
                        }
    			    }
    			}
    			itr += 1;    			
    		}
    	}
    }

    return result;

}

vector<vector<vector<vector<double> > > > Im2Col::pad(vector<vector<vector<vector<double> > > > images,
	                                                  int padding_height, int padding_width)
{
    vector<vector<vector<vector<double> > > > copied_images = images;
    int batch_size = copied_images.size();
	int n_channels = copied_images[0].size();
	int img_height = copied_images[0][0].size();
	int img_width = copied_images[0][0][0].size();

	for(int i=0; i<batch_size; i++){
		for(int j=0; j<n_channels; j++){
			for (int k = 0; k < img_height; ++k)
			{
				std::vector<double> row = copied_images.at(i).at(j).at(k);
				auto it = row.begin();
				row.insert(it, padding_width, 0);

                it = row.end();
                row.insert(it, padding_width, 0);

				copied_images.at(i).at(j).at(k) = row;

			}
			auto cct_image = copied_images.at(i).at(j);			
			vector<vector<double> > top_padding(padding_height, vector<double> (img_width + 2*padding_width, 0.0));
			cct_image.insert(cct_image.end(), top_padding.begin(), top_padding.end());
			cct_image.insert(cct_image.begin(), top_padding.begin(), top_padding.end());
			
			copied_images.at(i).at(j) = cct_image;

		}

	}
	return copied_images;

}

void print_2d(vector<vector<double> > tensor){
    int h = tensor.size();
	int w = tensor[0].size();
	for(int i=0; i<h; i++){
		for(int j=0; j<w; j++){
			cout << tensor.at(i).at(j) << " ";
		}
		cout << endl;
	}
}

void print_tensor(vector<vector<vector<vector<double> > > > tensor)
{
	int batch_size = tensor.size();
	int n_channels = tensor[0].size();
	int img_height = tensor[0][0].size();
	int img_width = tensor[0][0][0].size();

	for(int i=0; i<batch_size; i++){
		cout << "---" << "batch: " << i << endl;
		for(int j=0; j<n_channels; j++){
			for(int k=0; k<img_height; k++){
				cout << "[ ";
				for (int l = 0; l < img_width; ++l)
				{
					cout << tensor.at(i).at(j).at(k).at(l) << " ";
				}
				cout << " ]" << endl;
			}
			cout << endl;
		}
		cout << endl;
	}


}

int main()
{

    //std::random_device rd;  //Will be used to obtain a seed for the random number engine
    //std::mt19937 gen(rd()); //Standard mersenne_twister_engine seeded with rd()
    //std::uniform_real_distribution<> dis(1.0, 2.0);

	//double index = 0.0;
	vector<vector<vector<vector<double> > > > 
	    images(128, vector<vector<vector<double> > >(64, vector<vector<double> > (128, vector<double> (128, 0.002))));

	//print_tensor(images);
	//cout << endl;

	Im2Col im2col;
	//auto pad = im2col.pad(images, 1, 1);
	//print_tensor(pad);
	
	//cout << endl;

	//print_tensor(images);

	//cout << endl;

	auto out = im2col.im2col(images, 3, 3, 0, 0, 1, 1);
	//print_2d(out);

	
}

