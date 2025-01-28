
import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    
    # Input
    to_input('sfcc.png', to='(-3,0,0)', width=6, height=6, name='input0'),
    to_input('sfcc.png', to='(-2.75,0,0)', width=6, height=6, name='input1'),
    to_input('sfcc.png', to='(-2.5,0,0)', width=6, height=6, name='input2'),

    # First Convolution Layer
    to_Conv("conv1", 81, 32, offset="(0,0,0)", to="(0,0,0)", height=27, depth=27, width=12, caption="Conv1\n32@3x3" ),
    to_Pool("pool1", h=27, c=32, offset="(2,0,0)", to="(conv1-east)", height=9, depth=9, width=12, caption="MaxPool\n3x3"),
    
    # Second Conv Layer
    to_Conv("conv2", 27, 64, offset="(1.5,0,0)", to="(pool1-east)", height=9, depth=9, width=12, caption="Conv2\n64@3x3" ),
    to_Pool("pool2", h=1, c=64, offset="(1.5,0,0)", to="(conv2-east)", height=1, depth=1, width=12, caption="Global\nMax Pool"),
    
    to_SoftMax("fc1", 64, offset="(2,0,0)", to="(pool2-east)", caption="FC1 (64)", width=1, height=1, depth=16),
    to_SoftMax("fc2", 32, offset="(1,0,0)", to="(fc1-east)", caption="FC2 (32)", width=1, height=1, depth=8),
    to_SoftMax("fc3", 3, offset="(1,0,0)", to="(fc2-east)", caption="FC3 (3)", width=1, height=1, depth=3),

    # Connection
    to_connection("conv1", "pool1"),
    to_connection("pool1", "conv2"),
    to_connection("conv2", "pool2"),
    to_connection("pool2", "fc1"),
    # to_connection("fc1", "fc2"),
    # to_connection("fc2", "fc3"),

    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
