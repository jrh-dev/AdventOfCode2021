import re

class reboot:
    def __init__(self, instructions, restriction):
        self.instruct = self._parse_instruct(instructions, restriction)
        self.reboot_steps = self._reboot_steps(self.instruct)
        self.turned_on = sum([self._on_off(s) for s in self.reboot_steps])        

    def _parse_instruct(self, instructions, restriction):
        rep = {"x=": "","y=": "","z=": "","..": ","," ": ",","on": "1","off": "-1",}
        rep = dict((re.escape(k), v) for k, v in rep.items()) 
        pattern = re.compile("|".join(rep.keys()))
        instruct = [pattern.sub(lambda m: rep[re.escape(m.group(0))], string) for string in input]
        instruct = [i.split(",") for i in instruct]
        for ii in range(len(instruct)):
            instruct[ii] = [int(i) for i in instruct[ii]]
        if restriction:
            instruct = [c for c in instruct if abs(c[1]) <= 50]
        return instruct

    def _overlap(self, c_a, c_b):
        out=[-c_b[0]]
        out.append(max(c_a[1],c_b[1]))
        out.append(min(c_a[2],c_b[2]))
        out.append(max(c_a[3],c_b[3]))
        out.append(min(c_a[4],c_b[4]))
        out.append(max(c_a[5],c_b[5]))
        out.append(min(c_a[6],c_b[6]))
        if (out[1] > out[2]) | (out[3] > out[4]) | (out[5] > out[6]):
            return None
        else:
            return out

    def _reboot_steps(self, ins):
        steps = []
        for i in ins:
            tmp_i = [i] if i[0] == 1 else []
            for step in steps:
                ol = self._overlap(i,step)
                if ol:
                    tmp_i += [ol]
            steps += tmp_i
        return steps

    def _on_off(self, s):
        return (s[0] * (s[2]-s[1]+1) * (s[4]-s[3]+1) * (s[6]-s[5]+1))

f = open("day_22.txt", "r")
input = f.read().split("\n")
f.close()

# part 1 answer
reboot(input,50).turned_on

# part 2 answer
reboot(input,None).turned_on
