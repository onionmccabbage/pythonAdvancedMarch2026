import asyncio
import timeit

async def main():
    '''Any function can be run asynchronously (async)'''
    await asyncio.sleep(1) # here would be a long running (blocking) process
    print('all done')

if __name__ == '__main__':
    # this is how we call n async function
    # asyncio.run( main() )
    start = timeit.default_timer()
    with asyncio.Runner() as runner:
        runner.run(main())
        runner.run(main())
        runner.run(main())
        runner.run(main())
        runner.run(main())
        runner.run(main())
    end = timeit.default_timer()
    print(f'{end-start}')