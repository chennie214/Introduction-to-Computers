{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "0610.py",
      "provenance": [],
      "authorship_tag": "ABX9TyNXwfpNv1RYyM2PtHIifvIL",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/chennie214/Introduction-to-Computers/blob/main/0610.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "70zBhNr27w3O",
        "outputId": "28e1db05-be89-4bae-d065-b17a88f15086"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1*1= 11*2= 21*3= 31*4= 41*5= 51*6= 61*7= 71*8= 81*9= 9\n",
            "2*1= 22*2= 42*3= 62*4= 82*5=102*6=122*7=142*8=162*9=18\n",
            "3*1= 33*2= 63*3= 93*4=123*5=153*6=183*7=213*8=243*9=27\n",
            "4*1= 44*2= 84*3=124*4=164*5=204*6=244*7=284*8=324*9=36\n",
            "5*1= 55*2=105*3=155*4=205*5=255*6=305*7=355*8=405*9=45\n",
            "6*1= 66*2=126*3=186*4=246*5=306*6=366*7=426*8=486*9=54\n",
            "7*1= 77*2=147*3=217*4=287*5=357*6=427*7=497*8=567*9=63\n",
            "8*1= 88*2=168*3=248*4=328*5=408*6=488*7=568*8=648*9=72\n",
            "9*1= 99*2=189*3=279*4=369*5=459*6=549*7=639*8=729*9=81\n"
          ]
        }
      ],
      "source": [
        "for i in range(1,10):\n",
        "  for j in range(1,10):\n",
        "    product=i*j\n",
        "    print('%d*%d=%2d' %(i,j,product),end=\"\")\n",
        "  print()"
      ]
    }
  ]
}