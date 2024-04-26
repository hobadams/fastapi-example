import {NextResponse, type NextRequest} from 'next/server'

export async function POST(request: NextRequest) {
  console.log('HEEEREE')

  try {
    const response = await fetch('http://127.0.0.1:8000/api/items/1243', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({name: 'testing the name here'}),
      cache: 'no-cache',
    })
    console.log({response})
    const test = await response.json()

    return NextResponse.json(test)
  } catch (error) {
    console.error('Error:', error)
  }
}

export async function GET(request: NextRequest) {
  return NextResponse.json({name: 'bob'})
}
