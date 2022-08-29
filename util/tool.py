class Tool:
    def get_data(self, filename):
        f = open(filename, mode='r', encoding='utf-8')
        data = []
        for line in f:
            l = tuple(line.strip().replace(' ', '').split(','))
            data.append(l)
        return data[1:]


if __name__ == '__main__':
   s = Tool().get_data('../data/login_data.csv')
   print(s)