import multiprocessing
import Queue

version = "0.1.0"

model = {
    'simulation_control':[
        
    ]
    'location': [

    ],
    'climate': [

    ]
}


def worker(q, worker):
    while True:
        try:
            fname, objs, group = q.get(timeout=4)
            create_file(fname, group, objs)
        except Queue.Empty:
            print(worker, " Worker finished")
            break

def create_file(fname, group, objs):
    source_files = []
    for obj in objs:
        class_source = generate_class(obj)
        source_files.append(class_source)

    source = generate_group(group, source_files)

    with open(f'../design_nest/{fname}.py', 'w') as f:
        f.write(source)