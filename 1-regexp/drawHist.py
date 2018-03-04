import matplotlib.pyplot as plt

with open('money2.txt') as fp:
    lines = fp.readlines();
    lines.pop();
    money = [int(x.strip()) for x in lines];


beforeSplitFig = plt.figure();
plt.hist(money);
plt.ticklabel_format(style='plain');
plt.xticks(rotation=80);
plt.title("Histogram wartości pieniężnych dla 2014 roku");
plt.tight_layout()
beforeSplitFig.savefig("beforeSplit.png");

higherThan1M = [];
lowerThan1M = [];

for value in money:
    if value < 1000000:
        lowerThan1M.append(value);
    else:
        higherThan1M.append(value);

lowerThan1MFig = plt.figure();
plt.hist(lowerThan1M);
plt.ticklabel_format(style='plain');
plt.title("Histogram wartości pieniężnych <1mln dla 2014 roku");
plt.xticks(rotation=80);
plt.tight_layout()
lowerThan1MFig.savefig("lowerThan1M.png");

higherThan1MFig = plt.figure();
plt.hist(higherThan1M);
plt.xticks(rotation=80);
plt.title("Histogram wartości pięniężnych >1mln dla 2014 roku");
plt.ticklabel_format(style='plain');
plt.tight_layout();
higherThan1MFig.savefig("higherThan1m.png");
